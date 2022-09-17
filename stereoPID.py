import config as cfg
from simple_pid import PID

pidx = PID(cfg.PID_P, cfg.PID_I, cfg.PID_D, setpoint=0)
pidy = PID(cfg.PID_P, cfg.PID_I, cfg.PID_D, setpoint=0)
pidx.output_limits = (-1, 1)
pidy.output_limits = (-1, 1)
pidx.sample_time = cfg.interval
pidy.sample_time = cfg.interval

def calculatePID(ptobj, pttgt):
    ptx = ptobj[0] - pttgt[0]
    pty = ptobj[1] - pttgt[1]
    controlx = pidx(ptx)
    controly = pidy(pty)
    return [controlx, controly]
