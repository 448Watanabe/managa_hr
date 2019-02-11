# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):
    first_name = models.CharField("student's first name", max_length = 256)
    last_name = models.CharField("student's last name", max_length = 256)
    email = models.EmailField("email address", max_length = 256, unique = True)
    phone = models.SmallIntegerField(unique = True) # ハイフンは含まないで入力ように設定
    password = models.CharField("password", max_length = 512)
    school_id = models.PositiveSmallIntegerField()
    grade = models.PositiveSmallIntegerField(unique = True)
    age = models.PositiveSmallIntegerField(null = False)
    bday = models.DateField(null = True)
    chara = models.TextField(null = True)
    flag = models.BooleanField(null = False, default = True) # 塾に所属しているか否か
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
    # created_date = models.DateTimeField(False, True, editable=False, default=datetime.now()) だとエラーになる
    def __str__(self):
        return "User name is {} {}.".format(self.first_name, self.last_name)
    


class Friend(models.Model):
    # student_id = models.SmallIntegerField(unique = True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null = False, related_name='%(class)s_student')
    # friend_id = models.SmallIntegerField(unique = True)
    friend = models.ForeignKey(Student, on_delete=models.CASCADE, null = False, related_name='%(class)s_friend')
    
    def __str__(self):
        return "{}".format(self.student)

class BelongSchool(models.Model):
    school_name = models.CharField(max_length = 256, null = False)
    department = models.CharField(max_length = 256, null = True)
    concentration = models.CharField(max_length = 256, null = True)
    My_choices = (
        ("A", "Art"),
        ("S", "Science"),
    )
    art_or_science = models.CharField(max_length = 1, choices= My_choices)
    deviation = models.PositiveSmallIntegerField(null = True, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])

    def __str__(self):
        return "{}".format(self.school_name)


class DesiredSchool(models.Model):
    # student_id = models.SmallIntegerField(unique = True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null = False)
    # school_id = models.SmallIntegerField(unique = True)
    school = models.ForeignKey(BelongSchool, on_delete=models.CASCADE, null = False)
    
    def __str__(self):
        return "{}".format(self.student)

    
