from django.db import models
from django.conf import settings
import os


class files(models.Model):
    file_up = models.FileField(upload_to="")
    time = models.DateTimeField(null=True, blank=True)
    """def __unicode__(self):
        return '%s' % (self.file_up.name)
    def delete(self,*args,**kwargs):
        try:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.file_up.name))
            super(files,self).delete(*args,**kwargs)
        except OSError:
            pass"""

