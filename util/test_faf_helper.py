from builtins import staticmethod


from touroptimizer_py_client.models.creator_setting import CreatorSetting


from touroptimizer_py_client.models.optimization_persistence_setting import OptimizationPersistenceSetting
from touroptimizer_py_client.models.optimization_persistence_stratgy_setting import OptimizationPersistenceStratgySetting
from touroptimizer_py_client.models.stream_persistence_stratgy_setting import StreamPersistenceStratgySetting
from touroptimizer_py_client.models.mongo_optimization_persistence_setting import MongoOptimizationPersistenceSetting
from pprint import pprint

class TestFAFHelper:
    
    @staticmethod
    def default_creator_settings(creator = "TEST_PY_FAF_CREATOR") -> CreatorSetting:
        creator_setting = CreatorSetting()
        
        creator_setting.creator = creator
        
        return creator_setting
    
    
    @staticmethod
    def default_optimization_persistence_settings(secret = "", save_only_result = False) -> OptimizationPersistenceSetting:

        #  Do we want to only save the result object?
        #save_only_result = False
        
        # Saving the element connections etc.
        opti_per_stat_setting =  OptimizationPersistenceStratgySetting(save_only_result=save_only_result)
        
                
        # Element connections usually make up most of the data size, therefore, when
        # targeting to not further process the result, it might be a good idea
        # to skip the connections saving to reduce space
        opti_per_stat_setting.save_connections = False
        
        # How to treat streams? For example, do we want to continuously write the
        # current progress into a database? Do we want to cycle the progress?
        save_progress = True;
        save_status = True;
        save_warning = True;
        save_error = True;
        
        stream_persistence_stratgy_setting = StreamPersistenceStratgySetting(
            save_progress=save_progress,
            save_status=save_status,
            save_warning = save_warning,
            save_error = save_error)

        stream_persistence_stratgy_setting.cycle_status = True;
        stream_persistence_stratgy_setting.cycle_progress = True;
        
       
        
        
        
        # A secret encrypting the content of the final snapshot/result. If empty, no encryption is used.
        # Important: Metadata and stream information like progress is always saved as decrypted clear text.
        # Attention: The secret is not saved by DNA evolutions. If you loose the secret, the file CAN NOT be restored.
        
        # Settings regarding encryption etc.
        #secret = ""
        
        # Do we want to save anything to the database?
        enable_persistence = True;

        mongo_settings = MongoOptimizationPersistenceSetting(
            enable_persistence = enable_persistence,
            secret = secret,
            optimization_persistence_stratgy_setting = opti_per_stat_setting,
            stream_persistence_stratgy_setting = stream_persistence_stratgy_setting)


        # Once saved, the snapshot/result will be deleted automatically after this time
        mongo_settings.expiry =  "PT48H"
        


        # Wrap
        # The general object wrapping the database persistence settings
        opti_per_setting = OptimizationPersistenceSetting()
        opti_per_setting.mongo_settings = mongo_settings
        
        return opti_per_setting
    
    
## ------- Main program -------
if __name__ == "__main__":
    test = TestFAFHelper.default_optimization_persistence_settings()
    pprint(test)
    
    test_2 = TestFAFHelper.default_creator_settings("hash:TEST")
    pprint(test_2)
    