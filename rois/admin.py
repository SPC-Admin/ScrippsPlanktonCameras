from django.contrib import admin
from rois.models import Image, HumanAnnotator, MachineAnnotator, Annotator, PlanktonCamera, Label, LabelInstance, TagSet, LabelSet, QueryRecord, Tag
from django_mptt_admin.admin import DjangoMpttAdmin

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = (
            'image_id',
            'timestamp',
            'camera',
            'image_width',
            'image_height',
            'major_axis_length',
            'minor_axis_length',
            'image_tag',
            'binary_image_tag',
            'boundary_image_tag',
            'features_tag'
    )
    
    fieldsets = [
            ('Image Information', {
                'fields': [
                    'image_id',
                    'camera',
                    'image_width',
                    'image_height',
                    'timestamp',
                    'major_axis_length',
                    'minor_axis_length'
                ]
            }),
            ('Tags and Labels', {
                'fields': [
                    'user_labels',
                    'machine_labels',
                    'tags'
                ]
            }),
            ('Images and Features', {
                'fields':[ 
                    (
                        'image_tag',
                        'binary_image_tag',
                        'boundary_image_tag'
                
                    ),
                    'features_tag'
                ],
            })
    ]

    list_display = (
            'image_id',
            'timestamp',
            'major_axis_length',
            'minor_axis_length'
    )

    list_filter = ['timestamp']

#class TagAdmin(DjangoMpttAdmin):
#    tree_auto_open = 0
#    list_display = ('name',)
#    ordering = ('name',)

@admin.register(LabelInstance)
class LabelInstanceAdmin(admin.ModelAdmin):

    readonly_fields = (
            'image',
            'label_set',
            'label',
            'confidence',
            'created',
            'annotator',
    )

    fields = (
            'image',
            'label_set',
            'label',
            'confidence',
            'created',
            'annotator',
    )

    list_display = (
            'get_image',
            'get_label_set',
            'label',
            'confidence',
            'created',
            'get_annotator',
    )

    def get_image(self,obj):
        return obj.image.image_id
    get_image.short_description = 'Image ID'


    def get_label_set(self,obj):
        return obj.label_set.submitted
    get_label_set.short_description = 'Label Set Submitted'
    
    def get_annotator(self,obj):
        return obj.annotator.user
    get_annotator.short_description = 'Annotator User'

@admin.register(TagSet)
class TagSetAdmin(admin.ModelAdmin):
    readonly_fields = (
            'started',
            'submitted',
            'machine_name',
            'image_list',
            'confidence_list',
            'query_path',
    )

    fields = (
            'tag',
            'user',
            'user_info',
            'machine_name',
            'is_machine',
            'started',
            'submitted',
            'query_path',
            'notes',
            'image_list',
            'confidence_list',
    )

    list_display = (
            'tag',
            'user',
            'is_machine',
            'machine_name',
            'started',
            'submitted',
            'images_per_second',
            'total_images',
            'total_time',
    )

@admin.register(LabelSet)
class LabelSetAdmin(admin.ModelAdmin):
    readonly_fields = (
            'started',
            'submitted',
            'machine_name',
            'image_list',
            'confidence_list',
            'query_path',
    )
   
    fields = (
            'label',
            'user',
            'user_info',
            'machine_name',
            'is_machine',
            'started',
            'submitted',
            'query_path',
            'notes',
            'image_list',
            'confidence_list',
    )

    list_display = (
            'label',
            'user',
            'is_machine',
            'machine_name',
            'started',
            'submitted',
            'images_per_second',
            'total_images',
            'total_time',
    )

@admin.register(QueryRecord)
class QueryRecordAdmin(admin.ModelAdmin):
    readonly_fields = (
            'path',
            'user',
            'submitted',
            'remote_addr',
            'user_agent'
    )
   
    fields = (
            'path',
            'user',
            'submitted',
            'remote_addr',
            'user_agent'
    )

    list_display = (
            'path',
            'user',
            'submitted',
            'remote_addr',
    )


# Register models without custom classes here.
admin.site.register(Label)
admin.site.register(Tag)
admin.site.register(PlanktonCamera)
admin.site.register(Annotator)
admin.site.register(MachineAnnotator)
admin.site.register(HumanAnnotator)
