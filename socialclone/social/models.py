# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comment(models.Model):
    comment_id_bin = models.BinaryField(primary_key=True, max_length=16, editable = False)
  #  comment_id_text = models.CharField(max_length=36, blank=True, null=True)
    post = models.ForeignKey('Repost', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Repost', models.DO_NOTHING, related_name='comment_user_set', blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'comment'
    
    
    def __str__(self):
        return str(uuid(self.comment_id_bin))
    
    def save(self, *args, **kwargs):
        my_uuid = uuid.uuid4()
        # if not self.user_id_text:
        #   self.user_id_text = my_uuid
        if not self.comment_id_bin:
            self.comment_id_bin = my_uuid.bytes
       
        super().save(*args, **kwargs)


class CommentLikes(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, comment_id) found, that is not supported. The first column is selected.
    comment = models.ForeignKey(Comment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comment_likes'
        unique_together = (('user', 'comment'),)


class CommentTag(models.Model):
    comment = models.ForeignKey(Comment, models.DO_NOTHING, blank=True, null=True)
    tag_name = models.ForeignKey('Tag', models.DO_NOTHING, db_column='tag_name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment_tag'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
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


class Follower(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, follower_id) found, that is not supported. The first column is selected.
    follower = models.ForeignKey('User', models.DO_NOTHING, related_name='follower_follower_set')

    class Meta:
        managed = False
        db_table = 'follower'
        unique_together = (('user', 'follower'),)


class Post(models.Model):
    post_id_bin = models.BinaryField(primary_key=True, max_length=16, editable = False)
    #post_id_text = models.CharField(max_length=36, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'post'

    def __str__(self):
        return str(uuid(self.post_id_bin))
    
    def save(self, *args, **kwargs):
        my_uuid = uuid.uuid4()
        # if not self.user_id_text:
        #   self.user_id_text = my_uuid
        if not self.post_id_bin:
            self.post_id_bin = my_uuid.bytes
       
        super().save(*args, **kwargs)

class PostLikes(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, post_id) found, that is not supported. The first column is selected.
    post = models.ForeignKey(Post, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post_likes'
        unique_together = (('user', 'post'),)


class PostTag(models.Model):
    post = models.ForeignKey('Repost', models.DO_NOTHING, blank=True, null=True)
    tag_name = models.ForeignKey('Tag', models.DO_NOTHING, db_column='tag_name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_tag'


class Repost(models.Model):
    post = models.ForeignKey(Post, models.DO_NOTHING, blank=True, null=True)
    reposted_from_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    reposted_by_user = models.ForeignKey('User', models.DO_NOTHING, related_name='repost_reposted_by_user_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repost'


class Tag(models.Model):
    tag_name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'tag'


class User(models.Model):
    user_id_bin = models.BinaryField(primary_key=True, max_length=16, editable=False)
    # user_id_text = models.CharField(max_length=36, blank=True, null=True)
    username = models.CharField(unique=True, max_length=30)
    email = models.CharField(unique=True, max_length=255)
    dob = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return uuid(self.user_id_bin)
    
    def save(self, *args, **kwargs):
        my_uuid = uuid.uuid4()
        # if not self.user_id_text:
        #   self.user_id_text = my_uuid
        if not self.user_id_bin:
            self.user_id_bin = my_uuid.bytes
       
        
        #print(self.user_id_bin, self.user_id_text)

        super().save(*args, **kwargs)

class UserFollowsTag(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    tag_name = models.ForeignKey(Tag, models.DO_NOTHING, db_column='tag_name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_follows_tag'
