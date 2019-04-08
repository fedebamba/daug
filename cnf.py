

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

    # 14 - partito
    "uub-estimation-entro+dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": True,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200
    },
    # 15 - partito
    "uub-estimation-max-of-both": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "using_max": True
        },
        "using_prior": True,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200
    },
    # 17
    "uub-entro+dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200
    },
    # 17
    "uub-entro": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-6,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200
    },
    "uub-entro+dist-more-daug": {
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
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 28,
            "gauss_mean": 0,
            "gauss_var": 0.15
        },
    },

    # 18
    "uub-dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "entropy_weight": 0,
            "distance_weight": 1,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "trans_config": {
            "rotation_degree": 5,
            "crop_amount": 28,
            "gauss_mean": 0,
            "gauss_var": 0.1
        },
    },
    # 20
    "uub-entro+dist-more-daug-no-rotation": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "trans_config": {
            "rotation": False,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.15
        },
    },
    # 21
    "uub-ee+dist-more-daug-no-gauss": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 1,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss": False,
        },
        "num_of_runs": 6,
    },
    # 22
    "uub-entro+dist-more-daug-2": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.15
        },

    },

    "uub-entro+dist-baseline-without-daug": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uub",
        "el_for_validation": 200,
        "daug": False,
        "num_of_runs": 6
    },


# NEW TESTS
    "uub-entropy-new-active-baseline": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": False,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
    },

    "uub-entropy-new-random-baseline": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_active": False,
        "daug": False,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
    },

    "uub-entropy-new-rotation_daug": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 7,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },

    "uub-entropy-new-gauss_daug": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation": False,
            "crop": False,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.1
        }
    },

    "uuu-entropy-new-crop_daug": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation": False,
            "crop_amount": 24,
            "flip": False,
            "gauss": False
        }
    },
    "uuu-entropy-new-flip_daug": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation": False,
            "crop": False,
            "flip": True,
            "gauss": False
        }
    },
    # ............................................................................
    "uuu-entropy-new-crop_daug-more-tries": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation": False,
            "crop_amount": 22,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-rotation_daug-more-tries": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 9,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-rotation_daug-crop_daug": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 5,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "flip": False,
            "gauss": False
        }
    },
    "uuu-entropy-new-gauss_daug-more-tries": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation": False,
            "crop": False,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.1
        }
    },
    "uuu-entropy-new-rotation_daug-crop_daug-flip_daug": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 7,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "flip": True,
            "gauss": False
        }
    },
    "uuu-entropy-new-rotation_daug-crop_daug-more-tries": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 7,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 5,
            "crop_amount": 24,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-rotation_daug-crop_daug-less-distortion": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 5,
            "crop_amount": 26,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-dist-and-max-of-both-new-rotation_daug-more-tries": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "distance_weight": 1,
            "using_max": True
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 9,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },
    "uuu-ee-new-rotation_daug": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 7,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 5,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },
    "uuu-ee-new-crop_daug": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 7,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation": False,
            "crop_amount": 24,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-ee-new-gauss_daug-less-noise": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 7,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation": False,
            "crop":False,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-entropy-new-rotation_daug-more-tries-same-distortion": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 5,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-rotation_daug-same-tries-more-distortion": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 5,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 9,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-crop_daug-more-tries-same-distortion": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "n":9,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation": False,
            "crop_amount": 24,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-rotation_daug-crop_daug-gauss_daug-even-less-distortion": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 4,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-entropy-test-for-exclusive-transformations": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "exclusive_transformations": True,
            "rotation_degree": 4,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-entropy-test-for-exclusive-transformations-more-tests": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 15,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "exclusive_transformations": True,
            "rotation_degree": 5,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-entropy-new-rotation_daug-crop_daug-gauss_daug-even-less-distortion-even-more-tries": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 15,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 4,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },
    "uuu-ee-new-rotation_daug-crop_daug-gauss_daug-even-less-distortion-even-more-tries": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 15,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 4,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },
    "uuu-ee-new-rotation_daug-crop_daug-gauss_daug-even-less-distortion": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 4,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-ee-and-dist-and-var-new-rotation_daug-crop_daug-gauss_daug-even-less-distortion-more-tries": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 1,
            "distance_weight": 1,
            "using_max": True
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 15,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 4,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },
    "uuu-entro-and-dist-and-var-new-rotation_daug-crop_daug-gauss_daug-even-less-distortion": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "distance_weight": 1,
            "using_max": True
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 4,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-entropy-test-for-exclusive-transformations-more-tests-more-noise": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 15,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "exclusive_transformations": True,
            "rotation_degree": 7,
            "crop_amount": 24,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-ee-test-for-exclusive-transformations-more-tests": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 15,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "exclusive_transformations": True,
            "rotation_degree": 5,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },
    "uuu-ee-test-for-exclusive-transformations-more-tests-9-tries": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "exclusive_transformations": True,
            "rotation_degree": 5,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-entropy-test-for-exclusive-transformations-9-tries-more-noise": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "exclusive_transformations": True,
            "rotation_degree": 7,
            "crop_amount": 24,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-ee-test-for-exclusive-transformations-9-tries-more-noise": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "exclusive_transformations": True,
            "rotation_degree": 7,
            "crop_amount": 24,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-entro-and-dist-new-rotation_daug-crop_daug-gauss_daug-even-less-distortion": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 1,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 4,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-dist-new-rotation_daug-crop_daug-gauss_daug-even-less-distortion": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 0,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 4,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },




    "uuu-var-new-rotation_daug-crop_daug-gauss_daug-even-less-distortion": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 1,
            "entropy_weight":0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "n": 9,
        "num_of_runs": 6,
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.05
        },
        "selection_trans_config": {
            "rotation_degree": 4,
            "crop_amount": 26,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-entropy-new-random-baseline-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-9,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_active": False,
        "daug": False,
        "num_of_runs": 6,
        "seeds":[413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159], #
        "full_classes": [0,2,3,4,5],
        "starting_indexes_location": "starting_indexes",
        "validation_indexes_location": "val_indexes",
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
    },
    "uuu-entropy-new-al-baseline-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": False,
        "num_of_runs": 6,
        "seeds":[413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159], #
        "full_classes": [0,2,3,4,5],
        "starting_indexes_location": "starting_indexes",
        "validation_indexes_location": "val_indexes",
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
    },

    "uuu-entropy-new-rotation_daug-7-degrees-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "seeds":[413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159], #
        "full_classes": [0,2,3,4,5],
        "starting_indexes_location": "starting_indexes",
        "validation_indexes_location": "val_indexes",
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "rotation_degree": 7,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-rotation_daug-5-degrees-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "seeds":[413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159], #
        "full_classes": [0,2,3,4,5],
        "starting_indexes_location": "starting_indexes",
        "validation_indexes_location": "val_indexes",
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "rotation_degree": 5,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-gauss_daug-005-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "seeds":[413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159], #
        "full_classes": [0,2,3,4,5],
        "starting_indexes_location": "starting_indexes",
        "validation_indexes_location": "val_indexes",
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "rotation": False,
            "crop": False,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.005
        }
    },

    "uuu-entropy-new-gauss_daug-01-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "seeds":[413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159], #
        "full_classes": [0,2,3,4,5],
        "starting_indexes_location": "starting_indexes",
        "validation_indexes_location": "val_indexes",
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "rotation": False,
            "crop": False,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.01
        }
    },

    "uuu-entropy-new-crop_daug-26-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "seeds":[413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159], #
        "full_classes": [0,2,3,4,5],
        "starting_indexes_location": "starting_indexes",
        "validation_indexes_location": "val_indexes",
        "trans_config": {
            "rotation_degree": 7,

            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "rotation": False,
            "crop_amount": 26,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-crop_daug-28-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 7,
        "seeds": [413853558, 1386890164, 3699572969, 2171801678, 1561786004, 1406464819, 2530787159],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "rotation": False,
            "crop_amount": 28,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-seed-test-bench-true-deterministic-true": {
        "epochs": 5,
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 3,
        "seeds": [0,0,0],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "rotation": False,
            "crop_amount": 28,
            "flip": False,
            "gauss": False
        },
    },


    "uuu-seed-test-bench-true-deterministic-false": {
        "epochs": 5,
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 3,
        "seeds": [0, 0, 0],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "rotation": False,
            "crop_amount": 28,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-rotation_daug-3-degrees-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 7,
        "seeds": [413853558, 1386890164, 3699572969, 2171801678, 1561786004, 1406464819, 2530787159],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "rotation_degree": 3,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-ee-new-rotation_daug-5-degrees-set-seed": {
        "af_config": {
            "using_ensemble_entropy": True,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 7,
        "seeds": [413853558, 1386890164, 3699572969, 2171801678, 1561786004, 1406464819, 2530787159],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "rotation_degree": 5,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-gauss_daug-015-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 7,
        "seeds": [413853558, 1386890164, 3699572969, 2171801678, 1561786004, 1406464819, 2530787159],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "exclusive_transformations": False,
            "rotation": False,
            "crop": False,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.015
        }
    },

    "uuu-entropy-new-crop_daug-28-set-seed-with-origin": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "seeds": [413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "exclusive_transformations": True,
            "original": True,
            "rotation": False,
            "crop_amount": 28,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-gauss_daug-005-set-seed-with-origin": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 7,
        "seeds": [0, 1, 2, 3, 4, 5, 6],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "exclusive_transformations": True,
            "original": True,
            "rotation": False,
            "crop": False,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.005
        }
    },


    "uuu-entropy-new-gauss_daug-002-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "seeds": [413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "exclusive_transformations": False,
            "original": False,
            "rotation": False,
            "crop": False,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.002
        }
    },

    # todo
    "uuu-entropy-new-rotation_daug-7-degrees-set-seed-9-dist": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "n": 9,
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "seeds": [413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "exclusive_transformations": True,
            "original": True,
            "rotation_degree": 7,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },

    #todo
    "uuu-entropy-new-flip_daug-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 6,
        "seeds": [413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "exclusive_transformations": False,
            "original": False,
            "rotation": False,
            "crop": False,
            "flip": True,
            "gauss": False
        }
    },

    "uuu-entropy-new-rotation_daug-2-degrees-set-seed": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "n": 5,
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 7,
        "seeds": [0, 1, 2, 3, 4, 5, 6],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "rotation_degree": 2,
            "crop": False,
            "flip": False,
            "gauss": False
        }
    },

    "uuu-entropy-new-gauss_daug-002-set-seed-with-origin": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-7,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_random": False,
        "daug": True,
        "num_of_runs": 7,
        "seeds": [0, 1, 2, 3, 4, 5, 6],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
        "selection_trans_config": {
            "exclusive_transformations": True,
            "original": True,
            "rotation": False,
            "crop": False,
            "flip": False,
            "gauss_mean": 0,
            "gauss_var": 0.002
        }
    },

    "uuu-entropy-new-random-baseline-set-seed-bench-true": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-9,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_active": False,
        "daug": False,
        "num_of_runs": 7,
        "seeds":[0,1,2,3,4,5,6],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
    },

    "uuu-entropy-new-random-baseline-set-seed-bench-false": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-9,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_active": False,
        "daug": False,
        "num_of_runs": 7,
        "seeds":[0,1,2,3,4,5,6],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
    },

    "uuu-entropy-new-random-baseline-set-other-seed-bench-false": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-9,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_active": False,
        "daug": False,
        "num_of_runs": 7,
        "seeds": [45, 90, 135, 180, 225, 270, 315],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
    },


    "uuu-entropy-new-random-baseline-unset-seed-bench-false": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-9,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_active": False,
        "daug": False,
        "num_of_runs": 7,
        "seeds": [],     # [413853558, 1386890164, 3699572969, 2171801678, 1406464819, 2530787159]
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
    },


    "uuu-entropy-new-random-baseline-set-seed-bench-false-not-det": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-9,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_active": False,
        "daug": False,
        "num_of_runs": 7,
        "seeds":[0,1,2,3,4,5,6],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
    },

    "uuu-entropy-new-random-baseline-set-seed-bench-true-not-det": {
        "af_config": {
            "using_ensemble_entropy": False,
            "varratio_weight": 0,
            "distance_weight": 1e-9,
            "using_max": False
        },
        "using_prior": False,
        "prior_baseline": False,
        "balanced": "uuu",
        "el_for_validation": .1,
        "execute_active": False,
        "daug": False,
        "num_of_runs": 7,
        "seeds":[0,1,2,3,4,5,6],
        "trans_config": {
            "rotation_degree": 7,
            "crop_amount": 24,
            "gauss_mean": 0,
            "gauss_var": 0.01
        },
    },

}






