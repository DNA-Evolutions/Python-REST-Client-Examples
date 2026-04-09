"""
Helper for configuring job persistence settings (fire-and-forget pattern).

Provides factory methods to create CreatorSetting and OptimizationPersistenceSetting
objects used when submitting optimization jobs that persist their results to a database.
Covers settings for encryption, stream persistence (progress/status/warnings/errors),
and automatic document expiry.
"""

from builtins import staticmethod


from touroptimizer_py_client.models.creator_setting import CreatorSetting


from touroptimizer_py_client.models.optimization_persistence_setting import OptimizationPersistenceSetting
from touroptimizer_py_client.models.optimization_persistence_strategy_setting import OptimizationPersistenceStrategySetting
from touroptimizer_py_client.models.stream_persistence_strategy_setting import StreamPersistenceStrategySetting
from touroptimizer_py_client.models.mongo_optimization_persistence_setting import MongoOptimizationPersistenceSetting
from pprint import pprint

class TestFAFHelper:
    """Creates default persistence and creator settings for job-based optimizations."""

    @staticmethod
    def default_creator_settings(creator: str = "TEST_PY_FAF_CREATOR") -> CreatorSetting:
        """
        Creates a CreatorSetting with the given creator identifier.

        The creator is used to tag jobs in the database, allowing later retrieval
        via list_jobs. Use the "hash:" prefix to store a hashed creator value.

        :param creator: Creator identifier string.
        :return: Configured CreatorSetting.
        """
        creator_setting = CreatorSetting()
        
        creator_setting.creator = creator
        
        return creator_setting
    
    
    @staticmethod
    def default_optimization_persistence_settings(secret: str = "", save_only_result: bool = False) -> OptimizationPersistenceSetting:
        """
        Creates default persistence settings for storing optimization results in MongoDB.

        Configures what to persist (result, streams), encryption, and document expiry.
        By default, connections are excluded to reduce storage size, and stream data
        (progress, status, warnings, errors) is persisted with cycling enabled.

        :param secret: Encryption secret for the result. Empty string means no encryption.
                       WARNING: The secret is NOT stored by DNA Evolutions -- if lost,
                       the encrypted result cannot be restored.
        :param save_only_result: If True, only the optimization result is saved (not the full config).
        :return: Configured OptimizationPersistenceSetting with MongoDB settings.
        """

        #  Do we want to only save the result object?
        #save_only_result = False
        
        # Saving the element connections etc.
        opti_per_stat_setting =  OptimizationPersistenceStrategySetting(save_only_result=save_only_result)
        
                
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
        
        stream_persistence_strategy_setting = StreamPersistenceStrategySetting(
            save_progress=save_progress,
            save_status=save_status,
            save_warning = save_warning,
            save_error = save_error)

        stream_persistence_strategy_setting.cycle_status = True;
        stream_persistence_strategy_setting.cycle_progress = True;
        
       
        
        
        
        # A secret encrypting the content of the final snapshot/result. If empty, no encryption is used.
        # Important: Metadata and stream information like progress is always saved as decrypted clear text.
        # Attention: The secret is not saved by DNA evolutions. If you loose the secret, the file CAN NOT be restored.
        
        # Settings regarding encryption etc.
        #secret = ""
        
        # Do we want to save anything to the database?
        enable_persistence = True;

        mongo_settings = MongoOptimizationPersistenceSetting(
            enable_persistence = enable_persistence,
            require_unique_ident_creator_combination = False,
            secret = secret,
            optimization_persistence_strategy_setting = opti_per_stat_setting,
            stream_persistence_strategy_setting = stream_persistence_strategy_setting)


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
    