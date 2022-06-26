from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel, FieldPanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from home import blocks


class HomePage(Page):

    max_count = 1
    template = 'home.html'
    
    jumbotron = StreamField(
        [
            
            ('jumbotron', blocks.HeadingBlock()),
        ],
        null=True,
        blank=True,
    )

    heading = models.CharField(max_length=250, null=True, blank=True, verbose_name='heading')
    carousel = StreamField(
        [
            
            ('carousel', blocks.CarouselBlock()),
        ],
        null=True,
        blank=True,
    )
    exhibition_index = models.ForeignKey(
        'home.ExhibitionIndex',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL,
        )
    exhibition_name = models.CharField(max_length=250, null=True, blank=True, default='View Exhibition', verbose_name='Title')


    card = StreamField(
        [
            
            ('card', blocks.CardBlock()),
        ],
        null=True,
        blank=True,
    )

    about_section = StreamField(
        [
            
            ('about_section', blocks.AboutBlock()),
        ],
        null=True,
        blank=True,
    )

    mission = StreamField(
        [
            
            ('mission', blocks.MissionBlock()),
        ],
        null=True,
        blank=True,
    )

    director = StreamField(
        [
            
            ('mission', blocks.DirectorBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('jumbotron'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('heading',),
                PageChooserPanel('exhibition_index'),
                FieldPanel('exhibition_name',),
             ]),
            StreamFieldPanel('carousel'),
            ], heading='Slide'),
        StreamFieldPanel('card'),
        StreamFieldPanel('about_section'),
        StreamFieldPanel('mission'),
        StreamFieldPanel('director'),
    ]


    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'


class ExhibitionIndex(Page):

    
    subpage_types = [
        
        'home.ExhibitionPage',
    ]

    template = 'exhibition_index.html'
    max_count = 1
    

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        all_posts = ExhibitionPage.objects.live().public().order_by('-first_published_at')

        

        paginator = Paginator(all_posts, 20)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        return context

    class Meta:
        verbose_name = 'Exhibition'



class ExhibitionPage(Page):
    parent_page_types = [
        
        'home.ExhibitionIndex',
    ]

    subpage_types = [
        
        'home.ExhibitionPage',
    ]

    template = 'exhibition_page.html'

    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )


    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('body'),
    ]


    class Meta:
        verbose_name = 'Exhibition'


class AboutPage(Page):

    template = 'about_page.html'

    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )


    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('body'),
    ]


    class Meta:
        verbose_name = 'About'

