import unittest
import numpy as np 
import os, sys
import torch
import shutil, time
import copy

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, path)

from haven import haven_utils as hu
from haven import haven_results as hr
from haven import haven_chk as hc
from haven import haven_jobs as hjb
from haven import haven_jupyter as hj

    # # return
    # exp_list = [{'model':{'name':'mlp', 'n_layers':30}, 
    #             'dataset':'mnist', 'batch_size':1}]
    # savedir_base = '/home/toolkit/home_mnt/data/experiments'
    # job_config = {
    #     'image': 'registry.console.elementai.com/mila.mattie_sandbox.fewshotgan/fewshot-gan',
    #     'data': ['mila.mattie_sandbox.fewshotgan.home:/home/toolkit/home_mnt'],

if __name__ == '__main__':
    # return
   
    job_config = {
        'image': 'registry.console.elementai.com/eai.issam/ssh',
        
        'data': ['c76999a2-05e7-4dcb-aef3-5da30b6c502c:/mnt/home',
                 '20552761-b5f3-4027-9811-d0f2f50a3e60:/mnt/results',
                 '9b4589c8-1b4d-4761-835b-474469b77153:/mnt/datasets'],

        'preemptable':True,
        'resources': {
            'cpu': 4,
            'mem': 8,
            'gpu': 1
        },
        'interactive': False,
    }

    exp_list = [{'model':{'name':'mlp', 'n_layers':20}, 
                'dataset':'mnist', 'batch_size':1}]
    savedir_base = '/mnt/results/test'

    
    jm = hjb.JobManager(exp_list=exp_list, 
                    savedir_base=savedir_base, 
                    workdir=os.path.dirname(os.path.realpath(__file__)),
                    job_config=job_config,
                    account_id='75ce4cee-6829-4274-80e1-77e89559ddfb',
                    )
    # get jobs              
    job_list_old = jm.get_jobs()

    # run single command
    savedir_logs = '%s/%s' % (savedir_base, np.random.randint(1000))
    os.makedirs(savedir_logs, exist_ok=True)
    command = 'echo 2'
    job_id = jm.submit_job(command,  workdir=jm.workdir, savedir_logs=savedir_logs)

    # get jobs
    job_list = jm.get_jobs()
    job = jm.get_job(job_id)
    assert job_list[0].id == job_id
    
    # jm.kill_job(job_list[0].id)
    # run
    print('jobs:', len(job_list_old), len(job_list))
    assert (len(job_list_old) + 1) ==  len(job_list)

    # command_list = []
    # for exp_dict in exp_list:
    #     command_list += []

    # hjb.run_command_list(command_list)
    # jm.launch_menu(command=command)
    jm.launch_exp_list(command='echo 2 -e <exp_id>', reset=1, in_parallel=False)
    
    assert(os.path.exists(os.path.join(savedir_base, hu.hash_dict(exp_list[0]), 'job_dict.json')))
    summary_list = jm.get_summary_list()
    print(hr.filter_list(summary_list, {'job_state':'SUCCEEDED'}))
    print(hr.group_list(summary_list, key='job_state', return_count=True))
    
    rm = hr.ResultManager(exp_list=exp_list, savedir_base=savedir_base,
                          account_id='75ce4cee-6829-4274-80e1-77e89559ddfb')
    rm_summary_list = rm.get_job_summary()

    db = hj.get_dashboard(rm,  wide_display=True)
    db.display()
    # assert(rm_summary_list['table'].equals(jm_summary_list['table']))
    
    # jm.kill_jobs()
    # assert('CANCELLED' in jm.get_summary()['status'][0])