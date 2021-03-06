# Generated by Django 4.0.2 on 2022-06-28 16:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_homepage_about_section_alter_homepage_carousel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='about_section',
            field=wagtail.core.fields.StreamField([('about_section', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=60, required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(page_type=['home.AboutPage'], required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Read More', max_length=40, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='director',
            field=wagtail.core.fields.StreamField([('mission', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(page_type=['home.AboutPage'], required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Continue Reading', max_length=40, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='mission',
            field=wagtail.core.fields.StreamField([('mission', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(page_type=['home.AboutPage'], required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=40, required=False))]))], blank=True, null=True),
        ),
    ]
