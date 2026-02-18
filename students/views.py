from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Achievement, Category


# ======================
# STUDENT LIST
# ======================
def student_list(request):
    query = request.GET.get("q")
    students = Student.objects.all()

    if query:
        students = students.filter(name__icontains=query)

    total_students = Student.objects.count()
    active_students = Student.objects.filter(status="Active").count()

    context = {
        "students": students,
        "total_students": total_students,
        "active_students": active_students,
    }

    return render(request, "studentlist.html", context)


# ======================
# ADD STUDENT
# ======================
def add_student(request):

    if request.method == "POST":

        Student.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            register_number=request.POST.get("register_number"),
            course=request.POST.get("course"),
            batch=request.POST.get("batch"),
            department=request.POST.get("department"),
            status=request.POST.get("status")
        )

        return redirect("student_list")

    return render(request, "add_student.html")


# ======================
# STUDENT DETAIL + ACHIEVEMENTS
# ======================
def student_detail(request, pk):

    student = get_object_or_404(Student, pk=pk)

    # VERY IMPORTANT LINE
    achievements = Achievement.objects.filter(student=student)

    context = {
        "student": student,
        "achievements": achievements
    }

    return render(request, "student_details.html", context)


# ======================
# EDIT STUDENT
# ======================
def edit_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.register_number = request.POST.get("register_number")
        student.course = request.POST.get("course")
        student.batch = request.POST.get("batch")
        student.department = request.POST.get("department")
        student.status = request.POST.get("status")

        student.save()

        return redirect("student_detail", pk=student.id)

    return render(request, "edit_student.html", {
        "student": student
    })



# ======================
# DELETE STUDENT
# ======================
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("student_list")


# ======================
# ADD ACHIEVEMENT
# ======================
def add_achievement(request, pk):
    student = get_object_or_404(Student, pk=pk)
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        category_id = request.POST.get("category")
        date = request.POST.get("date")
        proof = request.FILES.get("proof")   # ✅ IMPORTANT LINE

        category = Category.objects.get(id=category_id)

        Achievement.objects.create(
            student=student,
            title=title,
            description=description,
            category=category,
            date=date,
            proof=proof    # ✅ SAVE FILE
        )

        return redirect("student_detail", pk=pk)

    return render(request, "add_achievement.html", {
        "student": student,
        "categories": categories
    })

# ======================
# EDIT ACHIEVEMENT
# ======================
def edit_achievement(request, id):
    achievement = get_object_or_404(Achievement, id=id)
    categories = Category.objects.all()

    if request.method == "POST":
        achievement.title = request.POST.get("title")
        achievement.description = request.POST.get("description")

        category_id = request.POST.get("category")
        achievement.category = Category.objects.get(id=category_id)

        achievement.date = request.POST.get("date")

        # ✅ VERY IMPORTANT — handle proof file
        if request.FILES.get("proof"):
            achievement.proof = request.FILES.get("proof")

        achievement.save()

        return redirect("student_detail", pk=achievement.student.id)

    return render(request, "edit_achievement.html", {
        "achievement": achievement,
        "categories": categories
    })




# ======================
# DELETE ACHIEVEMENT
# ======================
def delete_achievement(request, id):

    achievement = get_object_or_404(Achievement, id=id)

    student_id = achievement.student.id

    achievement.delete()

    return redirect("student_detail", pk=student_id)


# ======================
# APPROVE / REJECT ACHIEVEMENT
# ======================
def update_achievement_status(request, id, status):

    achievement = get_object_or_404(Achievement, id=id)

    achievement.status = status

    achievement.save()

    return redirect("student_detail", pk=achievement.student.id)
