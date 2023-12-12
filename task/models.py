from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import TimestampModel

User = get_user_model()


class Task(TimestampModel):
    """
    Team class that extends the TimeStampedModel.
    This class represents a task model with additional timestamp fields.
    """
    author = models.ForeignKey(User, verbose_name=_('author'), related_name='task_author', on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=254)
    description = models.TextField(_('description'), blank=True)
    completed = models.BooleanField(_('completed'), default=False)

    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    def __str__(self):
        return f'id_{self.id}: {self.title[:50]}'
