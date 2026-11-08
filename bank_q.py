import simpy
import random
import statistics

# Simulation parameters
ARRIVAL_RATE = 8
SERVICE_RATE = 10
SIMULATION_TIME = 10000
WARM_UP_TIME= 1000
MEASUREMENT_TIME = SIMULATION_TIME - WARM_UP_TIME
NUMBER_OF_RUNS = 30

def run_simulation(seed):

    random.seed(seed)
    env = simpy.Environment()
    employee = simpy.Resource(env, capacity=2)

    waiting_times = []
    completed_customers = 0
    queue_area = 0
    busy_area = 0
    last_time = 0

    def monitor():
        nonlocal queue_area, busy_area, last_time

        while env.now < SIMULATION_TIME:
            yield env.timeout(1)

            measured_elapsed = max(
                0,
                env.now - max(last_time, WARM_UP_TIME)
            )

            queue_area += len(employee.queue) * measured_elapsed
            busy_area += len(employee.users) * measured_elapsed

            last_time = env.now
            
    def customer():
        nonlocal completed_customers

        arrival_time = env.now

        with employee.request() as request:
            yield request

            if arrival_time >= WARM_UP_TIME:
                waiting_times.append(env.now - arrival_time)

            service_time = random.expovariate(SERVICE_RATE / 60)

            yield env.timeout(service_time)

            if WARM_UP_TIME < env.now <= SIMULATION_TIME:
                completed_customers += 1

    def arrivals():
        while True:
            interarrival = random.expovariate(
                ARRIVAL_RATE / 60
            )

            yield env.timeout(interarrival)

            if env.now >= SIMULATION_TIME:
                break

            env.process(customer())

    env.process(monitor())
    env.process(arrivals())

    # Measure the first 8 hours
    env.run(until=SIMULATION_TIME)

    # Finish customers already in the system
    env.run()

    return {
    "waiting": statistics.mean(waiting_times),
    "queue_length": queue_area / MEASUREMENT_TIME,
    "utilization": busy_area /( MEASUREMENT_TIME * 2) * 100,
    "throughput": completed_customers / (MEASUREMENT_TIME / 60)
}


# Run 30 independent experiments
results = []

for run in range(NUMBER_OF_RUNS):
    result = run_simulation(42 + run)
    results.append(result)


# Calculate averages
avg_waiting = statistics.mean(
    r["waiting"] for r in results
)

avg_queue = statistics.mean(
    r["queue_length"] for r in results
)

avg_utilization = statistics.mean(
    r["utilization"] for r in results
)

avg_throughput = statistics.mean(
    r["throughput"] for r in results
)


# Display results
print("\n========== M/M/2 RESULTS ==========")
print(f"Number of experiments: {NUMBER_OF_RUNS}")
print(f"Average waiting time: {avg_waiting:.2f} minutes")
print(f"Average queue length: {avg_queue:.2f}")
print(f"Average server utilization: {avg_utilization:.2f}%")
print(f"Average throughput: {avg_throughput:.2f}")
print("===================================")