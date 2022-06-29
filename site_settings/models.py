from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField, RichTextField

@register_setting(icon='user')
class SocialMediaSettings(BaseSetting):
    title = models.CharField(max_length=100, null=True, blank=True, default='Join Us on', help_text='Title')
    instagram = models.URLField(max_length=100, default='www.instagram.com/', null=True, blank=True, help_text='Instagram URL')
    facebook = models.URLField(max_length=100, default='www.facebook.com/', null=True, blank=True, help_text='Facebook URL')
    twitter = models.URLField(max_length=100, default='www.twitter.com/', null=True, blank=True, help_text='Twitter URL')
    pinterest = models.URLField(max_length=100, default='www.pinterest.com/', null=True, blank=True, help_text='Pinterest URL')
    linkedin = models.URLField(max_length=100, default='www.linkedin.com/', null=True, blank=True, help_text='Linkedin URL')
    whatsapp = models.CharField(max_length=100, default='Enter your WhatsApp number', null=True, blank=True, help_text='Whatsapp Number')
    
    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('instagram'),
            FieldPanel('facebook'),
            FieldPanel('twitter'),
            FieldPanel('pinterest'),
            FieldPanel('linkedin'),
            FieldPanel('whatsapp'),
        ], heading="Social Media")
        ]

    class Meta:
        verbose_name = 'Social Media Channel'


@register_setting
class SiteSettings(BaseSetting):
    site_name = models.CharField(max_length=100, null=True, blank=True, help_text='Your website name')
    site_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        help_text='Your website logo',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)
    show_in_menu_bar = models.BooleanField(default=False, blank=True, help_text='Select to show logo in menu bar', verbose_name='Menu Logo',)
    show_title_in_menu_bar = models.BooleanField(default=False, blank=True, help_text='Select to show Title in menu bar', verbose_name='Menu Title',)

    panels = [
        MultiFieldPanel([
            FieldPanel('site_name'),
            FieldPanel('show_title_in_menu_bar'),
            ]),
        
        MultiFieldPanel([
            ImageChooserPanel('site_logo'),
            FieldPanel('show_in_menu_bar'),
            FieldPanel('caption'),
        ], heading="Website Image")
        

        ]

    class Meta:
        verbose_name = 'Site Settings'




@register_setting(icon='search')
class GoogleMapSetting(BaseSetting):
    api_key = models.CharField(max_length=100, null=True, blank=True, verbose_name='Google Maps API Key', help_text='The API Key used for Google Maps')
    map_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Map Title', help_text='Map Title for Screen readers, ex: Map to Goodale Park')
    place_id = models.CharField(max_length=100, null=True, blank=True, verbose_name='Google Place ID', help_text='Requires API Key to use place ID')
    map_zoom_level = models.IntegerField(null=True, verbose_name='Map zoom level', blank=True, help_text='Requires API Key to use zoom. 1: World, 5: Landmass/Continent, 10: City, 15: Streets, 20: Buildings')
    search = models.CharField(blank=True, verbose_name='Search', help_text='Address or search term used to find your location on the map', max_length=250)

    


    panels = [
        MultiFieldPanel([
            FieldPanel('api_key'),
            FieldPanel('search'),
            FieldPanel('map_title'),
            FieldPanel('place_id'),
            FieldPanel('map_zoom_level'),
            ], heading='Settings for Google Map'),
        ]

    class Meta:
        verbose_name = 'Google Map Settings'


@register_setting(icon='group')
class AdmissionSetting(BaseSetting):
    title = models.CharField(max_length=100, default='Admission', null=True, blank=True,)
    body = RichTextField(blank=True)


    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('body'),
            ])
        ]

    class Meta:
        verbose_name = 'Admission'



@register_setting(icon='home')
class AddressSetting(BaseSetting):
    address = RichTextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
    phone_number = models.CharField(max_length=50, null=True, verbose_name='Phone Number', blank=True,)


    panels = [
        MultiFieldPanel([
            FieldPanel('address'),
            FieldPanel('phone_number'),
            ImageChooserPanel('image'),
        ])
    ]

    class Meta:
        verbose_name = 'Address'



@register_setting(icon='time')
class HourSetting(BaseSetting):
    time_and_date = RichTextField(verbose_name='Time and Day', blank=True,)


    panels = [
        MultiFieldPanel([
            FieldPanel('time_and_date'),
        ])
    ]

    class Meta:
        verbose_name = 'Day and Time'


