from tkinter import W
from tkinter.messagebox import NO


WARRIOR = "Warrior"
LEADER = "Leader"
NOBLE = "Noble"
DIPLOMAT = "Diplomat"
MERCHANT = "Merchant"
STUDENT = "Student"
ARTISAN = "Artisan"
PRIEST = "Priest"
WORKER = "Worker"
ROGUE = "Rouge"
BANDIT = "Bandit"

themes = [WARRIOR, LEADER, NOBLE, DIPLOMAT, MERCHANT, STUDENT, ARTISAN, WORKER, ROGUE, BANDIT, PRIEST]
linked = {
    WARRIOR: [LEADER, BANDIT, WORKER],
    LEADER: [NOBLE, WARRIOR, BANDIT],
    NOBLE: [DIPLOMAT, LEADER],
    DIPLOMAT: [NOBLE, MERCHANT, LEADER, PRIEST],
    MERCHANT: [ARTISAN, WORKER, NOBLE],
    STUDENT: [PRIEST, ARTISAN],
    PRIEST: [STUDENT, WORKER, DIPLOMAT],
    WORKER: [STUDENT, ARTISAN, WARRIOR, ROGUE],
    ROGUE: [WORKER, ARTISAN, NOBLE, MERCHANT, BANDIT],
    BANDIT: [WORKER, LEADER, WARRIOR, MERCHANT, ROGUE],
    ARTISAN: [WORKER, MERCHANT, STUDENT]
}

RELATIONSHIPS = {
    WARRIOR: {
        LEADER: 3,
        WARRIOR: -1,
        ARTISAN: -1,
        WORKER: 1,
        NOBLE: 2
    },
    LEADER: {
        WARRIOR: 2,
        NOBLE: 2,
        ROGUE: -1,
        BANDIT: -2,
        LEADER: 2
    },
    NOBLE: {
        WARRIOR: 1,
        DIPLOMAT: 2,
        MERCHANT: 1,
        ARTISAN: 1,
        PRIEST: 2,
        ROGUE: -2,
        BANDIT: -3,
    },
    DIPLOMAT: {
        LEADER: 2,
        NOBLE: 2,
        PRIEST: 2,
        STUDENT: 1,
        DIPLOMAT: -1
    },
    MERCHANT: {
        ROGUE: -3,
        BANDIT: -3,
        ARTISAN: 2,
        WORKER: 1,
        NOBLE: 1,
        WARRIOR: 1,
        MERCHANT: -2
    },
    STUDENT: {
        WORKER: 3,
        WARRIOR: -1,
        LEADER: 1,
        DIPLOMAT: 2,
        PRIEST: 3,
        ROGUE: 1,
        BANDIT: -1,
        ARTISAN: 1,
        STUDENT: 2
    },
    ARTISAN: {
        WORKER: 2,
        ROGUE: -2,
        MERCHANT: 2,
        NOBLE: 1,
        LEADER: 1,
        ARTISAN: 1
    },
    WORKER: {
        WARRIOR: 2,
        LEADER: 3,
        DIPLOMAT: -1,
        BANDIT: -2,
        PRIEST: 2,
    },
    ROGUE: {
        WORKER: 1,
        MERCHANT: -3,
        LEADER: -1,
        NOBLE: -2,
        STUDENT: 1,
        ARTISAN: -1,
        ROGUE: -1
    },
    BANDIT: {
        WARRIOR: -2,
        LEADER: 2,
        NOBLE: -3,
        MERCHANT: -3,
        ARTISAN: -2,
        WORKER: -1,
        ROGUE: 1,
        BANDIT: -3
    },
    PRIEST: {
        LEADER: 1,
        STUDENT: 2,
        WORKER: 3,
        BANDIT: -1,
        NOBLE: 1,
        PRIEST: 3
    }
}