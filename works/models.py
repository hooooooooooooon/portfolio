from django.db import models

class Work(models.Model):

    """Model Definition for Work"""

    main_title = models.CharField(max_length=140)
    sub_title = models.CharField(max_length=140)
    theme = models.CharField(max_length=40)
    category = models.CharField(max_length=50)
    company = models.CharField(max_length=40)
    project_summary = models.CharField(max_length=255)
    role = models.PositiveIntegerField()
    sido = models.CharField(max_length=80)
    sigungu = models.CharField(max_length=80)
    address_1 = models.CharField(max_length=140)
    address_2 = models.CharField(max_length=140)
    site_plan = models.CharField(max_length=40)
    use = models.CharField(max_length=40)
    project_type = models.CharField(max_length=40)
    result = models.CharField(max_length=80)
    design_period = models.CharField(max_length=40)
    construction_period = models.CharField(max_length=40)
    site_area = models.DecimalField(max_digits = 12, decimal_places = 4)
    coverage_area = models.DecimalField(max_digits = 12, decimal_places = 4)
    gross_floor_area = models.DecimalField(max_digits = 12, decimal_places = 4, verbose_name="GFA")
    stories = models.IntegerField()
    project_introduction = models.CharField(max_length=255)
    project_prologue = models.CharField(max_length=255)
    project_site_description = models.CharField(max_length=255)
    project_design_strategy = models.CharField(max_length=255)
    project_analysis = models.CharField(max_length=255)
    design_concept = models.CharField(max_length=255)
    retail_design_strategy = models.CharField(max_length=255)
    amenity_design_strategy = models.CharField(max_length=255)
    unit_planning = models.CharField(max_length=255)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

