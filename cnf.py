

stuff = {
    "bbb-none-max-of-both": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "using_max": True
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced:": "bbb",
        "el_for_validation": .1
    },

    "bbb-none-entro+dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced:": "bbb",
        "el_for_validation": .1
    },

    #############################################################################################################
    "uuu-baseline-entro+dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": True,
        "prior_baseline": True,
        "balanced:": "uuu",
        "el_for_validation": .1
    },

    "uuu-baseline-max-of-both": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "using_max": True
        },
        "using_prior": True,
        "prior_baseline": True,
        "balanced:": "uuu",
        "el_for_validation": .1
    },

    "uuu-estimation-entro+dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": True,
        "prior_baseline": False,
        "balanced:": "uuu",
        "el_for_validation": .1
    },

    "uuu-estimation-max-of-both": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "using_max": True
        },
        "using_prior": True,
        "prior_baseline": False,
        "balanced:": "uuu",
        "el_for_validation": .1
    },

    "uuu-none-entro+dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced:": "uuu",
        "el_for_validation": .1
    },

    "uuu-none-max-of-both": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "using_max": True
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced:": "uuu",
        "el_for_validation": .1
    },

    "test-ensemble-entropy": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced:": "uuu",
        "el_for_validation": .1,
        "daug": False
    },
    "test-ensemble-entropy": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced:": "uuu",
        "el_for_validation": .1,
        "daug": False
    },
    "uub-ee-distance-daug": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced:": "uub",
        "el_for_validation": 200,
        "daug": True
    },

    "uub-ee-distance": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced:": "uub",
        "el_for_validation": 200,
        "daug": False
    },

    "uub-ee-daug": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced:": "uub",
        "el_for_validation": 200,
        "daug": True
    },

    "uub-ee": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced:": "uub",
        "el_for_validation": 200,
        "daug": False
    },
}
