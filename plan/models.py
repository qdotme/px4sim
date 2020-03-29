from django.db import models

# Create your models here.
class FlightPlan(models.Model):
    fileType = models.CharField(max_length=8, default="Plan")
    version = models.PositiveIntegerField(default=1)
    groundStation = models.CharField(max_length=16, default="PX4Sim MIT CAOS")


class FlightPlanGeoFence(models.Model):
    plan = models.OneToOneField(
        FlightPlan,
        on_delete=models.CASCADE,
        primary_key=True
    )
    version = models.PositiveIntegerField(default=2)


class FlightPlanRallyPoints(models.Model):
    plan = models.OneToOneField(
        FlightPlan,
        on_delete=models.CASCADE,
        primary_key=True
    )
    version = models.PositiveIntegerField(default=2)


class FlightPlanMission(models.Model):
    plan = models.OneToOneField(
        FlightPlan,
        on_delete=models.CASCADE,
        primary_key=True
    )
    version = models.PositiveIntegerField(default=2)

    groundSpeed = models.DecimalField(default=15, max_digits=5, decimal_places=2)
    hoverSpeed = models.DecimalField(default=5, max_digits=5, decimal_places=2)

    firmwareType = models.PositiveIntegerField(default=12)
    vehicleType = models.PositiveIntegerField(default=2)


class FlightPlanCommand(models.Model):
    mission = models.ForeignKey(
        FlightPlanMission,
        on_delete=models.CASCADE,
    )

    command = models.PositiveIntegerField()
    frame = models.PositiveIntegerField()

    autoContinue = models.BooleanField(default=True)
    type = models.CharField(max_length=16, default="SimpleItem")
    AMSLAltAboveTerrain = models.FloatField(default=None)
    Altitude = models.FloatField(default=None)
    AltitudeMode =