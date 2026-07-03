import asyncio
import random


class DeviceSimulator:

    def __init__(self, manager):
        self.manager = manager

    async def start(self):

        try:
            while True:

                device = random.choice(
                    self.manager.get_all_devices()
                )

                new_status = not device["status"]

                updated_device = self.manager.update_device(
                    device["id"],
                    new_status
                )

                state = self.get_state_text(
                    updated_device["type"],
                    updated_device["status"]
                )

                print(
                    f"[SIMULATOR] "
                    f"{updated_device['name']} | "
                    f"{state} | "
                    f"Current: {updated_device['current_power']}W | "
                    f"Rated: {updated_device['rated_power']}W | "
                    f"Runtime: {updated_device['total_runtime']}s | "
                    f"Energy: {updated_device['energy_today']:.6f} kWh | "
                    f"{updated_device['last_updated']}"
                )

                await asyncio.sleep(
                    random.randint(3, 5)
                )

        except asyncio.CancelledError:
            print("\n[SIMULATOR] Simulation stopped.")

    def get_state_text(self, device_type, status):

        if device_type == "Door":
            return "OPEN" if status else "CLOSED"

        return "ON" if status else "OFF"