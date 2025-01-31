import asyncio
import argparse
from main import PQCSimulation

async def run_simulation(args):
    simulation = PQCSimulation()
    
    if args.phase == 'all':
        await simulation.run_complete_simulation()
    elif args.phase == 'design':
        await simulation._phase_one_design_and_implementation()
    elif args.phase == 'security':
        await simulation._phase_two_security_analysis()
    elif args.phase == 'compliance':
        await simulation._phase_three_compliance_audit()
    elif args.phase == 'performance':
        await simulation._phase_four_performance_simulation()
    else:
        print(f"Unknown phase: {args.phase}")

def main():
    parser = argparse.ArgumentParser(description='Post-Quantum Cryptography Simulation CLI')
    parser.add_argument(
        '--phase',
        choices=['all', 'design', 'security', 'compliance', 'performance'],
        default='all',
        help='Simulation phase to run'
    )
    
    args = parser.parse_args()
    asyncio.run(run_simulation(args))

if __name__ == '__main__':
    main()
