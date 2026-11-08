# Bank Queue Simulation

## Project Description
This project simulates a bank queue using Python and SimPy. It compares two queueing models: M/M/1 and M/M/2.

## Simulation Parameters
- Arrival rate: 8 customers per hour
- Service rate: 10 customers per hour per employee
- Simulation time: 10,000 minutes
- Warm-up period: 1,000 minutes
- Measurement period: 9,000 minutes
- Independent experiments: 30

## Models
- M/M/1: One employee serves customers.
- M/M/2: Two employees serve customers from one shared queue.

## Results

| Measure | M/M/1 | M/M/2 |
|---|---:|---:|
| Average waiting time | 24.57 min | 1.15 min |
| Average queue length | 3.26 | 0.15 |
| Server utilization | 80.30% | 39.82% per employee |
| Throughput | 7.96 | 7.92 customers/hour |

## Files
- `bank_q.py`: Python simulation code.
- `bank_q copy.py`: Duplicate of the simulation code.
- `Bank_q_simulation_results.txt`: Results from both models.

## Technologies
- Python
- SimPy
## How to Run the Simulation

### Requirements
- Python 3
- SimPy library

### Install SimPy
Open a terminal and run:

```bash
pip install simpy
```

### Run the simulation
1. Download or clone this GitHub repository.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python bank_q.py
```

### Note
The current `bank_q.py` file runs the M/M/2 simulation with two employees.

The final results for both M/M/1 and M/M/2 are available in `Bank_q_simulation_results.txt`.
