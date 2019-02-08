

stuff = {
    #1
    "bbb-none-max-of-both": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "using_max": True
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "bbb",
        "el_for_validation": .1
    },
    #2
    "bbb-none-entro+dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "bbb",
        "el_for_validation": .1
    },

    #3
    "uuu-baseline-entro+dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": True,
        "prior_baseline": True,
        "balanced": "uuu",
        "el_for_validation": .1
    },
    #4
    "uuu-baseline-max-of-both": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "using_max": True
        },
        "using_prior": True,
        "prior_baseline": True,
        "balanced": "uuu",
        "el_for_validation": .1
    },
    #############################################################################################################
    # 5
    "uuu-estimation-entro+dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": True,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1
    },
    # 6
    "uuu-estimation-max-of-both": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "using_max": True
        },
        "using_prior": True,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1
    },
    # 7
    "uuu-none-entro+dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1
    },
    # 8
    "uuu-none-max-of-both": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "using_max": True
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1
    },
    # 8 - bis
    "test-ensemble-entropy": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "daug": False
    },
    # 9
    "uub-ee-distance-daug": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "daug": True
    },
    # 10
    "uub-ee-distance": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "daug": False
    },
    # 11
    "uub-ee-daug": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "daug": True
    },
    # 12
    "uub-ee": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "daug": False
    },
}
