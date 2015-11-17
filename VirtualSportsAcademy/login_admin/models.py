from django.db import models

class AcademyOnboarding(models.Model):
    acd_reg_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=50, blank=True, null=True)
    estd = models.DateField(blank=True, null=True)
    address = models.ForeignKey('Address', db_column='address', blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    contact_no = models.BigIntegerField(blank=True, null=True)
    email_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academy_onboarding'


class AcademySports(models.Model):
    acd_reg_id = models.ForeignKey(AcademyOnboarding)
    sports_id = models.ForeignKey('Sports')

    class Meta:
        managed = False
        db_table = 'academy_sports'
        unique_together = [ 'acd_reg_id', 'sports_id']


class Address(models.Model):
    address_id = models.CharField(primary_key=True, max_length=20)
    country = models.ForeignKey('Country', db_column='country', blank=True, null=True)
    province = models.ForeignKey('Province', db_column='province', blank=True, null=True)
    city = models.ForeignKey('City', db_column='city', blank=True, null=True)
    street1 = models.CharField(max_length=30, blank=True, null=True)
    street2 = models.CharField(max_length=30, blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.ForeignKey(AuthGroup)
    permission_id = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = ['group_id', 'permission_id']


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = ['content_type_id', 'codename']


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.ForeignKey(AuthUser)
    group_id = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = ['user_id', 'group_id']


class AuthUserUserPermissions(models.Model):
    user_id = models.ForeignKey(AuthUser)
    permission_id = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = ['user_id', 'permission_id']


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=20, blank=True, null=True)
    country = models.ForeignKey('Country', db_column='country', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = ['app_label', 'model']


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gender(models.Model):
    gender_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gender'


class Level(models.Model):
    level_id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'level'


class Onboarding(models.Model):
    reg_id = models.CharField(primary_key=True, max_length=100)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.ForeignKey(Gender, db_column='gender', blank=True, null=True)
    email_id = models.CharField(max_length=100, blank=True, null=True)
    contact_no = models.BigIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    sports = models.ForeignKey('Sports', db_column='sports', blank=True, null=True)
    total_yrs_exp = models.IntegerField(blank=True, null=True)
    sec_ques_id = models.ForeignKey('SecurityQuestions', db_column='sec_ques1', blank=True, null=True)
    sec_ans1 = models.CharField(max_length=100, blank=True, null=True)
    sec_ques_id = models.ForeignKey('SecurityQuestions', db_column='sec_ques2', blank=True, null=True)
    sec_ans2 = models.CharField(max_length=100, blank=True, null=True)
    address = models.ForeignKey(Address, db_column='address', blank=True, null=True)
    role = models.ForeignKey('Role', db_column='role', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onboarding'


class Province(models.Model):
    province_id = models.IntegerField(primary_key=True)
    province_name = models.CharField(max_length=20, blank=True, null=True)
    country = models.ForeignKey(Country, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'


class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class SecurityQuestions(models.Model):
    sec_ques_id = models.AutoField(primary_key=True)
    sec_ques = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_questions'


class Sports(models.Model):
    sports_id = models.IntegerField(primary_key=True)
    sports_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports'


class Team(models.Model):
    reg_id = models.ForeignKey(Onboarding)
    name = models.CharField(max_length=50)
    level = models.ForeignKey(Level, db_column='level', blank=True, null=True)
    yrs_of_exp = models.IntegerField(blank=True, null=True)
    period_from = models.DateField(blank=True, null=True)
    period_to = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=30, blank=True, null=True)
    achievements = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'
        unique_together = ['reg_id', 'name']