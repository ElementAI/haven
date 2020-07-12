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
from haven import haven_ork as ho
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
    exp_list = [{'model':{'name':'mlp', 'n_layers':30}, 
                'dataset':'mnist', 'batch_size':1}]
    savedir_base = '/mnt/home/results/test'
    # get this with 'echo $ORG_NAME'
    org_name = 'eai'
    # get this with 'echo $ACCOUNT_NAME'

    job_config = {
        'image': 'registry.console.elementai.com/eai.issam/ssh',
        'data': ['c76999a2-05e7-4dcb-aef3-5da30b6c502c:/mnt/home'],
        'preemptable':True,
        'resources': {
            'cpu': 4,
            'mem': 8,
            'gpu': 1
        },
        # 'role':'eai.issam.role',
        'interactive': False,
    }

    jm = hjb.JobManager(exp_list=exp_list, 
                    savedir_base=savedir_base, 
                    workdir=os.path.dirname(os.path.realpath(__file__)),
                    job_config=job_config,
                    account_id='75ce4cee-6829-4274-80e1-77e89559ddfb',
                    role_id='0b3991cb-4c6c-4765-8305-eb54e44b2020'
                    )
    # get jobs              
    job_list_old = jm.get_jobs()

    # run single command
    savedir = '%s/%s' % (savedir_base, np.random.randint(1000))
    os.makedirs(savedir, exist_ok=True)
    command = 'echo 2 1>%s/logs.txt 2>%s/err.txt' % (savedir,savedir)
    job_id = jm.submit_job(command, savedir=None)

    # get jobs
    job_list = jm.get_jobs()
    job = jm.get_job(job_id)
    assert job_list[0].id == job_id
    
    jm.kill_job(job_list[0].id)
    # run
    print('jobs:', len(job_list_old), len(job_list))
    assert (len(job_list_old) + 1) ==  len(job_list)

    # command_list = []
    # for exp_dict in exp_list:
    #     command_list += []

    # hjb.run_command_list(command_list)

    jm.launch_exp_list(command='echo 2 -e <exp_id>')
    
    assert(os.path.exists(os.path.join(savedir_base, hu.hash_dict(exp_list[0]), 'job_dict.json')))
    jm_summary_list = jm.get_summary()
    rm = hr.ResultManager(exp_list=exp_list, savedir_base=savedir_base)
    rm_summary_list = rm.get_job_summary(account_id='75ce4cee-6829-4274-80e1-77e89559ddfb',
                                         role_id='0b3991cb-4c6c-4765-8305-eb54e44b2020')
    assert(rm_summary_list['table'].equals(jm_summary_list['table']))

    jm.kill_jobs()
    assert('CANCELLED' in jm.get_summary()['status'][0])