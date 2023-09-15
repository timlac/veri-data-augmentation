import opensmile


class SmileProcess:

    smile_lld = opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPSv02,
        feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
    )

    smile_func = opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPSv02,
        feature_level=opensmile.FeatureLevel.Functionals,
    )

    @classmethod
    def process_lld(cls, path):
        df = cls.smile_lld.process_file(path)

        # Drop the 'file' part of the MultiIndex
        df.reset_index(level='file', drop=True, inplace=True)

        return df

    @classmethod
    def process_func(cls, path):
        return cls.smile_func.process_file(path)
