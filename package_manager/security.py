import hashlib
import json
from typing import Any, Dict


class SecurityError(Exception):
    pass


class PackageSigner:
    """Handles cryptographic signing of .forgepkg manifests."""

    @staticmethod
    def sign_manifest(manifest_data: Dict[str, Any], private_key: str) -> str:
        """
        Mock implementation of cryptographic signing.
        In production, this would use sigstore or ECDSA signatures.
        """
        # A mock deterministic hash simulating a signature
        content_string = json.dumps(manifest_data, sort_keys=True) + private_key
        return hashlib.sha256(content_string.encode("utf-8")).hexdigest()


class PackageVerifier:
    """Verifies cryptographic signatures and handles security reviews."""

    @staticmethod
    def verify_manifest(manifest_data: Dict[str, Any], signature: str, public_key: str) -> bool:
        """
        Mock implementation of signature verification.
        """
        expected_sig = PackageSigner.sign_manifest(manifest_data, public_key)
        if expected_sig != signature:
            raise SecurityError(
                "Invalid package signature. The package may have been tampered with."
            )
        return True

    @staticmethod
    def review_permissions(requested_permissions: list[str]) -> None:
        """
        Checks if the requested permissions are excessively broad or require manual approval.
        """
        dangerous_permissions = ["fs:root", "network:all", "process:exec"]
        for perm in requested_permissions:
            if perm in dangerous_permissions:
                # This could trigger a prompt or log a severe warning
                pass
