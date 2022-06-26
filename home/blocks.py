from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.templatetags.wagtailcore_tags import richtext



class LinkStructValue(blocks.StructValue):

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None



class HeadingBlock(blocks.StructBlock):

    jumbotron = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('title', blocks.CharBlock(required=False, max_length=40)),
                ('description', blocks.RichTextBlock(required=False, features=['h1','h2','h3','h4','h5','h6','hr','bold','italic','link','code','superscript','subscript','strikethrough','blockquote',],)),
                ('color', blocks.CharBlock(required=False, default='#000000', max_length=40, help_text="Enter a hexdecimal color for the background e.g #000000")),
                ('text_color', blocks.CharBlock(required=False, default='#ffffff', max_length=40, help_text="Enter a hexdecimal color for the text e.g #000000 or red")),
                ('button_page', blocks.PageChooserBlock(required=False)),
                ('button_url', blocks.URLBlock(required=False)),
                ('button_text', blocks.CharBlock(required=False, default='Read More', max_length=40)),
            ]
        )
    )


    class Meta:
        template = "blocks/jumbotron_text_block.html"
        icon = "list-ul"
        label = "Heading"
        max_num = 1



class CarouselBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=['bold','italic'])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=False, default='Read More', max_length=40)


    class Meta:
        template = "blocks/carousel.html"
        icon = "plus"
        label = "Carousel"



class AboutBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=['bold','italic'])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=False, default='Read More', max_length=40)


    class Meta:
        template = "blocks/about_section.html"
        label = "About"



class MissionBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=['bold','italic'])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=False, default='Read More', max_length=40)


    class Meta:
        template = "blocks/mission.html"
        label = "Mission"


class DirectorBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=['bold','italic'])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=False, default='Read More', max_length=40)


    class Meta:
        template = "blocks/director_block.html"
        label = "Mission"


class CardBlock(blocks.StructBlock):

    select = blocks.BooleanBlock(required=False, blank=True, help_text='Select to use 2 columns', verbose_name='Two Columns',)

    card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('title', blocks.CharBlock(required=False, max_length=40)),
                ('description', blocks.RichTextBlock(required=False, features=['h1','h2','h3','h4','h5','h6','hr','bold','italic','link','code','superscript','subscript','strikethrough','blockquote',],)),   
                ('button_page', blocks.PageChooserBlock(required=False)),
                ('button_url', blocks.URLBlock(required=False)),
                ('button_text', blocks.CharBlock(required=False, default='Read More', max_length=40)),
            ]
        )
    )


    class Meta:
        template = "blocks/card_block.html"
        icon = "list-ul"
        label = "Card Block"
        max_num = 1
