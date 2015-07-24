from models import Tag


def do_the_tags_magic(tags):
    tags = tags.strip().split(';')
    values = []

    for tag in tags:
        try:
            values.append(Tag.objects.get(tag_text=tag).pk)
        except Tag.DoesNotExist:
            new_tag = Tag(tag_text=tag)
            new_tag.save()
            values.append(new_tag.pk)

    return values
