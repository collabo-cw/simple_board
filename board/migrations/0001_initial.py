# Generated by Django 4.2.14 on 2024-07-29 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('notice', '공지사항'), ('general', '일반 게시판'), ('qna', '질문 게시판')], help_text='카테고리', max_length=20, verbose_name='카테고리')),
                ('title', models.CharField(help_text='게시글 제목', max_length=200, verbose_name='제목')),
                ('content', models.TextField(help_text='게시글 내용', verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='생성일', verbose_name='작성일')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='수정일', verbose_name='수정일')),
                ('view_count', models.PositiveIntegerField(default=0, help_text='조회수', verbose_name='조회수')),
                ('is_activate', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('author', models.ForeignKey(help_text='작성자(유저)', on_delete=django.db.models.deletion.CASCADE, related_name='boards', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='첨부파일', upload_to='attachments/', verbose_name='첨부파일')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, help_text='업로드 생성일', verbose_name='업로드 일시')),
                ('order', models.PositiveIntegerField(default=0, help_text='첨부파일 순서', verbose_name='순서')),
                ('board', models.ForeignKey(help_text='게시글', on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='board.board', verbose_name='게시글')),
            ],
        ),
    ]
