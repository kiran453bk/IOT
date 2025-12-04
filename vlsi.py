# ------------------------------------------------------
# VLSI Block Performance Analysis Tool
# ------------------------------------------------------

class ChipBlock:
    def __init__(self, name, delay, dynamic_power, leakage_power, area):
        self.name = name
        self.delay = delay                     # in nanoseconds
        self.dynamic_power = dynamic_power     # in mW
        self.leakage_power = leakage_power     # in mW
        self.area = area                       # in mm^2

    # 1. Compute performance index (example formula)
    # Higher PI → better performance
    # PI = (1 / delay) * 100  -- simple normalized value
    def performance_index(self):
        try:
            return (1 / self.delay) * 100
        except ZeroDivisionError:
            return float('inf')

    # 2. Compute power density = (dynamic + leakage) / area
    def power_density(self):
        total_power = self.dynamic_power + self.leakage_power
        try:
            return total_power / self.area
        except ZeroDivisionError:
            return float('inf')

    # 3. Detect timing violation
    # If delay > target_clock_period → violation
    def has_timing_violation(self, target_clock_period):
        return self.delay > target_clock_period

    # Display block summary
    def report(self):
        print(f"----- Block: {self.name} -----")
        print(f"Delay           : {self.delay} ns")
        print(f"Dynamic Power   : {self.dynamic_power} mW")
        print(f"Leakage Power   : {self.leakage_power} mW")
        print(f"Area            : {self.area} mm^2")
        print(f"Performance Index: {self.performance_index():.2f}")
        print(f"Power Density    : {self.power_density():.2f} mW/mm^2")
        print("----------------------------------\n")


# ------------------------------------------------------
# Example Usage
# ------------------------------------------------------

if __name__ == "__main__":
    # Example blocks
    block1 = ChipBlock("ALU", 1.2, 15, 2, 0.8)
    block2 = ChipBlock("FIR_Filter", 2.5, 22, 3, 1.0)
    block3 = ChipBlock("Controller", 0.9, 10, 1.5, 0.5)

    blocks = [block1, block2, block3]

    # Generate reports
    for b in blocks:
        b.report()

    # Check timing violations
    target_clock_period = 1.5   # ns
    print("Timing Violation Check:")
    for b in blocks:
        if b.has_timing_violation(target_clock_period):
            print(f"❌ {b.name} violates timing!")
        else:
            print(f"✅ {b.name} meets timing!")
