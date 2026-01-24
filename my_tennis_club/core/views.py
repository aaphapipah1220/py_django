from django.shortcuts import render, redirect
from core.models import Leads, LeadsSource, DetailChannel, CustomersStatus, Programs, StudentAdvisor, Trial, Location, Teacher, Level, ClassType
from django.utils import timezone
from django.http import JsonResponse

def leads_create(request):
    lead_sources = LeadsSource.objects.all().order_by("id")
    detail_channels = DetailChannel.objects.all().order_by("id")
    customers_status = CustomersStatus.objects.all().order_by("id")
    programs = Programs.objects.all().order_by("id")
    student_advisor = StudentAdvisor.objects.all().order_by("id")

    if request.method == "POST":
        Leads.objects.create(
            leads_in_period = request.POST.get("leads_in_period") or timezone.now(),

            lead_source_id = int(request.POST.get("lead_source_id")),
            detail_channel_id = int(request.POST.get("detail_channel_id")),

            parents_name = request.POST.get("parents_name"),
            phone_number_of_parents = request.POST.get("phone_number_of_parents"),
            email = request.POST.get("email"),
            student_name = request.POST.get("student_name"),
            student_aged = request.POST.get("student_aged"),
            date_of_birth = request.POST.get("date_of_birth"),
            address = request.POST.get("address"),
            school = request.POST.get("school"),

            customer_status_id = int(request.POST.get("customer_status_id")),
            program_id = int(request.POST.get("program_id")),
            student_advisor_id = int(request.POST.get("student_advisor_id")),

            created_at = timezone.now(),

        )
        return redirect("leads_create")
    
    return render(request, "core/input_new_leads_form.html", {
        "lead_sources": lead_sources,
        "detail_channels": detail_channels,
        "customers_status": customers_status,
        "programs": programs,
        "student_advisor": student_advisor,
    })

def trial_create(request):
    leads = Leads.objects.all().order_by("student_name")
    trial_location = Location.objects.all().order_by("id")
    teacher = Teacher.objects.all().order_by("id")
    level = Level.objects.all().order_by("id")
    program = Programs.objects.all().order_by("id")
    class_type = ClassType.objects.all().order_by("id")

    if request.method == "POST":
        Trial.objects.create(
            coding_experience = request.POST.get("coding_experience"),
            purpose = request.POST.get("purpose"),
            date_and_time = request.POST.get("date_and_time"),

            lead_id=int(request.POST.get("lead_id")),
            trial_location_id=int(request.POST.get("location_id")),
            teacher_trial_id=int(request.POST.get("teacher_id")),
            level_trial_id=int(request.POST.get("level_id")),
            program_trial_id=int(request.POST.get("program_id")),
            class_type_id=int(request.POST.get("class_type_id")),

            room = request.POST.get("room"),
            created_at = timezone.now(),
        )
        return redirect("trial_create")

    return render(request, "core/input_trial_form.html", {
        "leads": leads,
        "trial_location": trial_location,
        "teacher_trial": teacher,
        "level_trial": level,
        "program_trial": program,
        "class_type": class_type,
    })

def get_lead_detail(request, lead_id):
    try:
        lead = Leads.objects.get(id=lead_id)
        data = {
            "student_aged": lead.student_aged,
            "school": lead.school,
            "detail_channel": lead.detail_channel.name if lead.detail_channel else ""
        }
        return JsonResponse(data)
    except Leads.DoesNotExist:
        return JsonResponse({"error": "Lead not found"}, status=404)
