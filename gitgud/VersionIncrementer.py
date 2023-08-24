from re import sub

class VersionIncrementer:
    def increment(self, version, semantic_part):
        semantic_part = semantic_part.lower()
        if semantic_part == 'patch':
            return self.patch(version)

        if semantic_part == 'minor':
            return self.minor(version)

        if semantic_part == 'major':
            return self.major(version)

    def major(self, version):
        pieces = version.split('.')
        major = sub(r'[^0-9]', '', pieces[0])
        major_prefix = sub(r'^([^0-9]*)[0-9]*', r'\1', pieces[0])
        new_major = int(major) + 1
        return major_prefix + str(new_major) + '.0.0'

    def minor(self, version):
        pieces = version.split('.')
        major = pieces[0]
        minor = pieces[1]
        new_minor = int(minor) + 1
        return major + '.' + str(new_minor) + '.0'

    def patch(self, version):
        pieces = version.split('.')
        major = pieces[0]
        minor = pieces[1]
        patch = pieces[2]
        new_patch = int(patch) + 1
        return major + '.' + minor + '.' + str(new_patch)
