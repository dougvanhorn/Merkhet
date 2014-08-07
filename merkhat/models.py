from django.contrib.auth.models import User
from django.db import models

# Always give your classes a Docstring.  Document the purpose.  Future you will
# thank you.  PEP-8: http://legacy.python.org/dev/peps/pep-0008/


class Project(models.Model):
    """Defines a project the team is working on.

    Collects tasks for billing.
    """
    # Attributes first.
    project = models.CharField(max_length=60)

    # The meta class if you need it.
    class Meta:
        # Watch your indentation, it defines scope.  Also, make sure you're not
        # inserting Tabs (\t).  Spaces only.
        #
        # This isn't necessary, it will pluralize Project to Projects.
        # You usually define this when you have Country to Countrys, which
        # should be Countries.  And you don't need to capitalize.
        # See: https://docs.djangoproject.com/en/dev/ref/models/options/#verbose-name-plural
        #verbose_name_plural = "Projects"
        
        # Generally speaking, you don't want to do this as it has the
        # unintended consequence of adding a SORT to your SQL queries, even
        # when you don't need it at all.  I'll typically leave the sorting
        # closer to the buisiness of how I'm using the data.
        ordering = ('project',)

    def __str__(self):  
        # Nice.  Note that in Python3, we use str instead of unicode.
        # http://www.diveintopython3.net/strings.html
        # Unicode is like timezones.  It's a pain in the ass.
        return self.project


class Task(models.Model):
    """I'm unsure of this model.  Is the intent to collect hours against a
    task & project?
    """
    # Generally, having an attribute the same name as the Model makes for odd
    # code.  E.g.,
    # task = Task.objects.all().first()
    # print(task.task)
    #
    # Maybe this is a name or title or description or text or ...
    task = models.CharField(max_length=60)

    class Meta:
        # See above notes.
        #verbose_name_plural = "Tasks"
        # See above notes.
        ordering = ('task',)

    def __str__(self):  
        return self.task


class HourEntry(models.Model):
    """HourEntry represents time worked against a project/task.
    """
    # Relationships
    # -------------------------------------------------------------------------
    # I would call this user.
    name = models.ForeignKey(User)

    project = models.ForeignKey(Project)
    task = models.ForeignKey(Task)


    # Attributes
    # -------------------------------------------------------------------------
    # TextField has no max_length, by definition.
    # https://docs.djangoproject.com/en/dev/ref/models/fields/#textfield
    # Okay, so it does, but it only impacts the admin UI.  Which is probably
    # best to avoid in here, or at least document that it's only UI related.
    notes = models.TextField()

    pub_date = models.DateField('Date Worked')

    hours = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,  # Stores NULL when empty.
        blank=True,  # Allows admin UI to be empty.
    )

    # Default the cost to NULL/empty instead of zero.  The purpose being that
    # 0 is actually a value and my have semantic meaning.  If we have nothing
    # to store, don't store anything.
    cost = models.IntegerField(
        null=True,  # Stores NULL when empty.
        blank=True,  # Allows admin UI to be empty.
    )

    billable = models.BooleanField(default=False)
    billed = models.BooleanField(default=False)


    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        # this is why we have verbose_name_plural...
        verbose_name_plural = "hour entries"


    # Methods
    # -------------------------------------------------------------------------
    def __str__(self):
        """Return the first line of notes if available.
        """
        if self.notes:
            lines = self.notes.splitlines()
            return lines[0]
        else:
            return self.notes

