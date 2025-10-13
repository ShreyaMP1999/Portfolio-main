import React from 'react';
import { personalInfoApi, achievementsApi } from '../services/api';
import { useApi } from '../hooks/useApi';
import { Award, Users, GraduationCap } from 'lucide-react';
import { LoadingSection, LoadingCard } from './LoadingSpinner';
import ErrorMessage from './ErrorMessage';

const About = () => {
  const { data: personalInfo, loading: personalLoading, error: personalError, refetch: refetchPersonal } = useApi(() => personalInfoApi.get());
  const { data: achievements, loading: achievementsLoading, error: achievementsError, refetch: refetchAchievements } = useApi(() => achievementsApi.getAll());

  const stats = [
    { number: '4+', label: 'Years Experience', icon: GraduationCap },
    { number: '3', label: 'Key Projects', icon: Award },
    { number: '50+', label: 'Bugs Resolved', icon: Users },
  ];

  // Handle loading state
  if (personalLoading || achievementsLoading) {
    return (
      <section id="about" className="py-20 bg-white">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
              About Me
            </h2>
            <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
          </div>
          <div className="grid lg:grid-cols-2 gap-12">
            <LoadingCard />
            <LoadingCard />
          </div>
        </div>
      </section>
    );
  }

  // Handle error state
  if (personalError || achievementsError) {
    return (
      <section id="about" className="py-20 bg-white">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
              About Me
            </h2>
            <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
          </div>
          <ErrorMessage 
            message={personalError || achievementsError} 
            onRetry={() => {
              if (personalError) refetchPersonal();
              if (achievementsError) refetchAchievements();
            }} 
          />
        </div>
      </section>
    );
  }

  if (!personalInfo) {
    return (
      <section id="about" className="py-20 bg-white">
        <div className="max-w-6xl mx-auto px-6">
          <ErrorMessage message="Personal information not found" onRetry={refetchPersonal} />
        </div>
      </section>
    );
  }

  return (
    <section id="about" className="py-20 bg-white">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
            About Me
          </h2>
          <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
        </div>

        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Column - Bio */}
          <div className="space-y-6">
            <p className="text-lg text-gray-700 leading-relaxed">
              {personalInfo.bio}
            </p>
            
            <p className="text-lg text-gray-700 leading-relaxed">
              With a strong foundation in both front-end and back-end technologies, I specialize in creating 
              intelligent solutions that bridge the gap between complex technical requirements and user-friendly interfaces. 
              My experience spans from enterprise applications at Accenture to cutting-edge AI/ML projects in healthcare.
            </p>

            {/* Stats */}
            <div className="grid grid-cols-3 gap-6 pt-8">
              {stats.map((stat, index) => {
                const Icon = stat.icon;
                return (
                  <div key={index} className="text-center">
                    <div className="flex justify-center mb-3">
                      <div className="p-3 bg-blue-50 rounded-lg">
                        <Icon className="w-6 h-6 text-blue-600" />
                      </div>
                    </div>
                    <div className="text-2xl font-bold text-gray-900 mb-1">
                      {stat.number}
                    </div>
                    <div className="text-sm text-gray-600 font-medium">
                      {stat.label}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Right Column - Achievements */}
          <div className="space-y-6">
            <h3 className="text-2xl font-bold text-gray-900 mb-6">
              Achievements & Leadership
            </h3>
            
            <div className="space-y-4">
              {achievements && achievements.length > 0 ? (
                achievements.map((achievement) => (
                  <div 
                    key={achievement.id}
                    className="bg-gray-50 rounded-lg p-6 hover:shadow-md transition-shadow duration-200"
                  >
                    <div className="flex items-start gap-4">
                      <div className="p-2 bg-blue-100 rounded-lg flex-shrink-0">
                        <Award className="w-5 h-5 text-blue-600" />
                      </div>
                      <div className="flex-1">
                        <h4 className="font-semibold text-gray-900 mb-1">
                          {achievement.title}
                        </h4>
                        <p className="text-sm text-blue-600 mb-2">
                          {achievement.organization} • {achievement.year}
                        </p>
                        <p className="text-sm text-gray-600">
                          {achievement.description}
                        </p>
                      </div>
                    </div>
                  </div>
                ))
              ) : (
                <div className="bg-gray-50 rounded-lg p-6">
                  <p className="text-gray-600 text-center">No achievements data available</p>
                </div>
              )}
            </div>

            {/* Quick Contact */}
            <div className="bg-blue-50 rounded-lg p-6 mt-8">
              <h4 className="font-semibold text-gray-900 mb-3">
                Let's Connect
              </h4>
              <p className="text-sm text-gray-600 mb-4">
                Always open to discussing new opportunities and interesting projects.
              </p>
              <div className="flex flex-col sm:flex-row gap-2 text-sm">
                <a 
                  href={`mailto:${personalInfo.email}`}
                  className="text-blue-600 hover:text-blue-700 font-medium transition-colors"
                >
                  {personalInfo.email}
                </a>
                <span className="hidden sm:inline text-gray-400">•</span>
                <a 
                  href={`tel:${personalInfo.phone}`}
                  className="text-blue-600 hover:text-blue-700 font-medium transition-colors"
                >
                  {personalInfo.phone}
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;