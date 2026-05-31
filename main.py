import time

class InvisibleTechnology:
    """
    Represents a technology that has become so integrated and reliable
    that its underlying complexity is no longer perceived by the user.
    """
    def __init__(self, name, setup_details):
        self.name = name
        self._setup_details = setup_details
        self._is_initialized = False

    def _perform_complex_setup(self):
        """
        Simulates the initial, complex setup or underlying infrastructure
        that users eventually take for granted. This is when the technology
        is 'visible' and new.
        """
        print(f"[{self.name}]: Initializing complex infrastructure: {self._setup_details}...")
        time.sleep(0.5) # Simulate work
        print(f"[{self.name}]: Infrastructure ready.")
        self._is_initialized = True

    def provide_service(self, user_request):
        """
        Provides the service, making the underlying technology 'invisible'.
        Users only interact with the desired outcome, not the mechanism.
        """
        if not self._is_initialized:
            # This block represents the phase where technology is new and its
            # setup is explicitly noticed by the user.
            self._perform_complex_setup()
            print(f"[{self.name}]: Initial setup complete. Now providing seamless service.")

        print(f"\nUser requests: '{user_request}'")
        print(f"[{self.name}]: Processing request via invisible technology...")
        time.sleep(0.2) # Simulate work
        print(f"[{self.name}]: Service '{user_request}' delivered seamlessly.")
        # After initial setup, the user only sees the result. The internal workings
        # (the 'technology') have become 'invisible' and assumed.

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Phase 1: Technology is new and its setup is visible ---")
    # When a technology is new, its underlying complexity and setup are often apparent.
    # Users are aware of the 'how'.
    electricity_grid = InvisibleTechnology(
        "Electricity Grid",
        "Power plants, transmission lines, substations, wiring..."
    )

    # First interaction: The underlying setup is performed and becomes visible.
    # The user is aware of the 'technology' behind the service.
    electricity_grid.provide_service("Power up my computer")

    print("\n--- Phase 2: Technology becomes invisible and assumed ---")
    # After initial setup and widespread adoption, the technology fades into the background.
    # Users only care about the outcome, not the mechanism. The 'technology' is now invisible.

    # Subsequent interactions: The setup is already done, so it's no longer 'visible'.
    # The user just expects the service to work without thinking about the grid.
    electricity_grid.provide_service("Turn on the lamp") # Technology is now invisible
    electricity_grid.provide_service("Charge my phone") # Technology is now invisible

    print("\n--- Another example: The Internet ---")
    internet = InvisibleTechnology(
        "Internet",
        "Routers, fiber optics, satellites, servers, protocols (TCP/IP, HTTP)..."
    )

    # First interaction with a new 'invisible' technology
    internet.provide_service("Browse dev.to")
    # Again, initial setup is visible, highlighting the underlying complexity.

    # Subsequent interactions: The Internet is now an assumed utility.
    # Its mechanisms are invisible; only the service is perceived.
    internet.provide_service("Send an email") # Invisible
    internet.provide_service("Stream a video") # Invisible

    print("\n--- Conclusion ---")
    print("The best technology becomes invisible when its underlying complexity")
    print("is abstracted away, and its service becomes an assumed utility.")
    print("Users interact with the desired outcome, not the technological mechanism.")
