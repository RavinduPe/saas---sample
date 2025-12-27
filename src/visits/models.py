from django.db import models

class PageVisit(models.Model):
    # db table
    path = models.TextField(blank=True, null=True) #col
    timestamp = models.DateTimeField(auto_now_add=True) #col

    def __str__(self):
        return f"{self.visitor_name} visited on {self.visit_date.strftime('%Y-%m-%d %H:%M:%S')}"