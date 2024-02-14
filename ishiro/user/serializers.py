from rest_framework import serializers
from ishiro.user.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """Create and return a new user"""
        password = validated_data.pop("password", None)
        email = validated_data.pop("email")
        
        return self.Meta.model.objects.create_user(email, password, **validated_data)

    def update(self, instance, validated_data):
        """Update an existing user"""
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)




    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "created_at",
            "updated_at",
        
        )
        extra_kwargs = {
            "password": {"required": True, "write_only": True, "style": {"input_type": "password"}},
            "last_name": {"required": True},
            "first_name": {"required": True},
            "is_active": {
                "read_only": True,
            },
        }


