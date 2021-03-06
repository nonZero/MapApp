from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from librarian.consts import MediaType


class Site(models.Model):
    name = models.CharField(_("name"), max_length=30, blank=False)
    additional_text = models.CharField(_('additional text'), max_length=30)
    location = models.PointField(_('location'))
    radius = models.PositiveSmallIntegerField(_('radius'), default=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("view_site", args=(self.pk,))

    def get_modal_url(self):
        return reverse("site_modal", args=(self.pk,))

    def get_edit_url(self):
        return reverse("update_site", args=(self.pk,))

    def get_delete_url(self):
        return reverse("delete_site", args=(self.pk,))

    class Meta:
        verbose_name = _('site')
        verbose_name_plural = _('sites')


class Collection(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=100)
    website_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = _('collection')
        verbose_name_plural = _('collections')

    def __str__(self):
        return self.title


class Content(models.Model):
    site = models.ForeignKey(Site, verbose_name="אתר מקושר",
                             related_name="contents")

    collection = models.ForeignKey(Collection, verbose_name="אוסף", null=True,
                                   blank=True)
    doc_id = models.CharField(max_length=100, null=True, blank=True)
    full_record = models.TextField()
    content_type = models.CharField("סוג התוכן", max_length=30,
                                    choices=MediaType.choices)
    name = models.CharField("שם או כותרת", max_length=30)
    creator = models.CharField("יוצר/ת", max_length=14, blank=True, null=True)
    creator_2 = models.CharField("יוצר/ת נוספ/ת", max_length=30, blank=True,
                                 null=True)
    performing = models.CharField("מבצע/ת", max_length=30, blank=True,
                                  null=True)
    description = models.CharField("תיאור התוכן", max_length=200, blank=True,
                                   null=True)
    link = models.URLField("קישור לתוכן")
    date = models.CharField("תאריך התוכן", blank=True, null=True,
                            max_length=40)

    def __str__(self):
        return "{}: {}".format(
                self.get_content_type_display(),
                self.name
        )

    def get_template_name(self):
        return "clientapp/content/_{}.html".format(self.content_type.lower())

    def get_absolute_url(self):
        return reverse("view_content", args=(self.site.id, self.pk))

    def get_edit_url(self):
        return reverse("update_content", args=(self.site.id, self.pk))

    def get_delete_url(self):
        return reverse("delete_content", args=(self.site.id, self.pk))

    class Meta:
        verbose_name = _("content")
        verbose_name_plural = "תכנים"

    def get_model_fields(self):
        result = []
        for field_instance in self._meta.get_fields():
            result.append(
                    (field_instance.name, getattr(self, field_instance.name)))

        return result
