

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
    }
}