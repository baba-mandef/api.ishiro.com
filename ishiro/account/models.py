from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from ishiro.extra.utils import generate_random_digits

class AccountMixin(models.Model):
    avatar = models.ImageField(null=True, upload_to="avatar/")
    activated = models.DateTimeField(null=True)
    deactivated = models.DateTimeField(null=True)
    verified = models.DateTimeField(null=True)
    verification_code = models.CharField(max_length=6)
    deactivated_reason = models.CharField(max_length=500, null=True blank=True)

    def activate(self):
        assert not self.activate, _("This account is already activated")
        self.is_active = True
        self.activated = now()
        self.deactivated = None
        self.deactivated_reason = None
        self.save()

    def deactivate(self, reason=None):
        assert not self.deactivated, _("This account is already deactivated")
        self.activated = None
        self.is_active = False
        self.deactivated = now()
        self.deactivated_reason = reason
        self.save()
    
    def get_verification_code(self):
        assert not self.verification_code, _("A verification code has already sent")
        self.verification_code = generate_random_digits(6)
        self.save()

    def verification(self, code=None):
        assert not self.verified, _("This account is already verified")
        if self.verification_code == code:
            self.verified = now()
            self.verification_code = None
            self.save()
        else:
            self.verified = None
            self.get_verification_code()
            self.save()
    
    class Meta():
        abstract = True
