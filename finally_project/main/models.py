from django.db import models

class People(models.Model):
    people = models.IntegerField()


class Feedback(models.Model):
    username = models.CharField(max_length=50)
    feedback = models.TextField(blank=False)


class Telegramm_Bots(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=150)
    time = models.CharField(max_length = 50)
    url = models.URLField()
    # photo = models.ImageField()
    def __str__(self):
        return self.title


class Discord_Bots(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=150)
    url = models.URLField()
    def __str__(self):
        return self.title

class Telegramm_Reviews(models.Model):
    username = models.CharField(max_length=50)
    text = models.TextField()
    reporter = models.ForeignKey(Telegramm_Bots, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username} - {self.reporter}'


class Discord_Reviews(models.Model):
    username = models.CharField(max_length=50)
    text = models.TextField()
    reporter = models.ForeignKey(Discord_Bots, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username} - {self.reporter}'