from rest_framework import serializers


try:

    from home.supervisor.models import Supervisor
    from home.sede.models import Sede
    from home.programa.models import Programa
    from home.nte.models import NTE
    from home.municipio.models import Municipio
    from home.faculdade.models import Faculdade
    from home.estagiario.models import Estagiario
    from home.edital.models import Edital
    from home.curso.models import Curso
    from home.estagiario.models import Estagiario

except:
    pass 

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Supervisor
        except:
            pass    
        fields = '__all__'

class SedeSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Sede
        except:
            pass    
        fields = '__all__'

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Programa
        except:
            pass    
        fields = '__all__'

class NTESerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = NTE
        except:
            pass    
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Municipio
        except:
            pass    
        fields = '__all__'

class FaculdadeSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Faculdade
        except:
            pass    
        fields = '__all__'

class EstagiarioSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Estagiario
        except:
            pass    
        fields = '__all__'

class EditalSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Edital
        except:
            pass    
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Curso
        except:
            pass    
        fields = '__all__'

class EstagiarioSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Estagiario
        except:
            pass    
        fields = '__all__'

