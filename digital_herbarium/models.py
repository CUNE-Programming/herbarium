from django.db import models
from rapidocr import RapidOCR


class Plant(models.Model):
    genus = models.CharField("genus", max_length=256, null=True, blank=True)
    species = models.CharField("species", max_length=256, null=True, blank=True)
    specimen_image = models.ImageField(upload_to="specimen_img/", null=True, blank=True)
    info_card_image = models.ImageField(upload_to="info_card_img/", null=True, blank=True)
    common_name = models.CharField("common_name", max_length=256, null=True, blank=True)
    year = models.CharField("year", max_length=256, null=True, blank=True)
    collector = models.CharField("collector", max_length=256, null=True, blank=True)

    # location of where the plant was collected from
    location = models.CharField("location", max_length=256, null=True, blank=True)
    cabinet = models.CharField("cabinet", max_length=256)
    drawer = models.CharField("drawer", max_length=256)
    ramarks = models.TextField("ramarks", null=True, blank=True)
    extra_info = models.CharField("extra_info", max_length=1024, null=True, blank=True)

    def __str__(self):
        return f"{self.genus} {self.species}"

    def prefil_fields(self):
        engine = RapidOCR()

        body, _ = engine(self.image)

        corpus = ""
        if body:
            text_only = [item[1] for item in body]
            for text in text_only:
                corpus += text + " "
                print(text)
        else:
            print("No text detected")

        print(corpus)
        return corpus
