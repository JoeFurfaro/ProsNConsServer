from django.db import models

class PCPro(models.Model):
    text = models.TextField()

class PCCon(models.Model):
    text = models.TextField()

class PCPost(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    title = models.TextField()
    author = models.TextField()
    pros = models.ManyToManyField("PCPro")
    cons = models.ManyToManyField("PCCon")

    def export(self):
        return {
            "title": self.title,
            "author": self.author,
            "pros": [pro.text for pro in self.pros.all()],
            "cons": [con.text for con in self.cons.all()]
        }
