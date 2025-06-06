from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100,
                                unique=True,
                                verbose_name='username')
    email = models.EmailField(unique=True, verbose_name='email')
    password = models.CharField(max_length=128, verbose_name='password')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='register_time')

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'user'

    def __str__(self):
        return self.username


class Note(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='notes',
                             verbose_name='使用者')
    # 自我關聯欄位 note_id（可用來實作子筆記或回覆），允許空值 #當初沒討論清楚 這邊似乎有點疑惑
    parent = models.ForeignKey('self',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               db_column='note_id',
                               related_name='children',
                               verbose_name='父筆記')
    title = models.CharField(max_length=200, verbose_name='筆記標題')
    content = models.TextField(verbose_name='筆記內容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    # 多對多關聯
    tags = models.ManyToManyField('Tag',
                                  through='NoteTag',
                                  related_name='notes',
                                  verbose_name='標籤')

    class Meta:
        db_table = 'notes'
        verbose_name = '筆記'
        verbose_name_plural = '筆記'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='標籤名稱')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='tags',
                             verbose_name='使用者')

    class Meta:
        db_table = 'tags'
        verbose_name = '標籤'
        verbose_name_plural = '標籤'
        unique_together = ('name', 'user')  # 保證每位使用者的 tag 名稱不重複

    def __str__(self):
        return self.name


class NoteTag(models.Model):
    note = models.ForeignKey(Note,
                             on_delete=models.CASCADE,
                             related_name='note_tags',
                             verbose_name='筆記')
    tag = models.ForeignKey(Tag,
                            on_delete=models.CASCADE,
                            related_name='note_tags',
                            verbose_name='標籤')

    class Meta:
        db_table = 'note_tags'
        unique_together = (('note', 'tag'), )
        verbose_name = '筆記-標籤 關聯'
        verbose_name_plural = '筆記-標籤 關聯'

    def __str__(self):
        return f'{self.note.title} – {self.tag.name}'
# NoteImage 模型用於存儲筆記中的圖片
class NoteImage(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='images', verbose_name='筆記')
    image = models.ImageField(upload_to='note_images/', verbose_name='圖片')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'note_images'
        verbose_name = '筆記圖片'
        verbose_name_plural = '筆記圖片'