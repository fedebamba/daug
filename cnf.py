

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

    #3 - fine
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
    #4 - fine
    "uuu-baseline-max-of-both": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "using_max": True
        },
        "epochs":100,
        "using_prior": True,
        "prior_baseline": True,
        "balanced": "uuu",
        "el_for_validation": .1
    },
    #############################################################################################################
    # 5 - fine
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
    # 6 - fine
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
    # 7 - fine
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
    # 8- fine
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
    # 8 - bis - partito
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
    # 9 -partito
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
    # 10 - partito
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
    # 11 - partito
    "uub-ee-daug": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 1e-6,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "daug": True
    },
    # 12 - partito
    "uub-ee": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 1e-6,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "daug": False
    },

    # 13 - partito
    "uub-test-using-marginals": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-6,
            "entropy_weight": 0,
            "marginals_weight": 1,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "daug": True
    },
}
