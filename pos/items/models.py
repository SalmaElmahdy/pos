from django.db import models


class Item(models.Model):
    """class represent an Item"""

    number = models.CharField("Number", max_length=50, unique=True)
    description = models.CharField("Description", max_length=100)
    price = models.IntegerField("Price", default=0.0)
    item_group = models.ForeignKey(
        "ItemGroup", verbose_name="Item Group", on_delete=models.CASCADE
    )


class ItemFamily(models.Model):
    """class represent an Item Family"""

    number = models.CharField("Number", max_length=50, unique=True)
    name = models.CharField("Name", max_length=100)


class ItemCategory(models.Model):
    """class represent an Item Category"""

    number = models.CharField("Number", max_length=50, unique=True)
    name = models.CharField("Name", max_length=100)
    family = models.ForeignKey(
        ItemFamily, verbose_name="Family", on_delete=models.CASCADE
    )


class ItemGroup(models.Model):
    """class represent an Item Group"""

    name = models.CharField("Name", max_length=50, unique=True)
    category = models.ForeignKey(
        ItemCategory, verbose_name="Category", on_delete=models.CASCADE
    )
