import React from 'react';
import { skillsApi } from '../services/api';
import { useApi } from '../hooks/useApi';
import { Code, Database, Cloud, Settings, Cpu, BarChart3 } from 'lucide-react';
import { LoadingSection, LoadingCard } from './LoadingSpinner';
import ErrorMessage from './ErrorMessage';

const Skills = () => {
  const { data: skills, loading, error, refetch } = useApi(() => skillsApi.getAll());

  // Icon mapping for skill categories
  const getSkillCategoryIcon = (category) => {
    const iconMap = {
      'Programming Languages': Code,
      'Web Technologies': Settings,
      'Databases': Database,
      'Cloud & DevOps': Cloud,
      'Tools & Platforms': Cpu,
      'AI/ML & Data': BarChart3,
    };
    return iconMap[category] || Code;
  };

  // Color mapping for skill categories
  const getSkillCategoryColor = (index) => {
    const colors = [
      "bg-blue-50 text-blue-600 border-blue-200",
      "bg-green-50 text-green-600 border-green-200", 
      "bg-purple-50 text-purple-600 border-purple-200",
      "bg-orange-50 text-orange-600 border-orange-200",
      "bg-gray-50 text-gray-600 border-gray-200",
      "bg-red-50 text-red-600 border-red-200"
    ];
    return colors[index % colors.length];
  };

  // Handle loading state
  if (loading) {
    return (
      <section id="skills" className="py-20 bg-gray-50">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
              Technical Skills
            </h2>
            <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              A comprehensive toolkit for building modern, scalable applications
            </p>
          </div>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <LoadingCard />
            <LoadingCard />
            <LoadingCard />
            <LoadingCard />
            <LoadingCard />
            <LoadingCard />
          </div>
        </div>
      </section>
    );
  }

  // Handle error state
  if (error) {
    return (
      <section id="skills" className="py-20 bg-gray-50">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
              Technical Skills
            </h2>
            <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
          </div>
          <ErrorMessage message={error} onRetry={refetch} />
        </div>
      </section>
    );
  }

  return (
    <section id="skills" className="py-20 bg-gray-50">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
            Technical Skills
          </h2>
          <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            A comprehensive toolkit for building modern, scalable applications
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {skills && skills.length > 0 ? (
            skills.map((skillCategory, index) => {
              const Icon = getSkillCategoryIcon(skillCategory.category);
              const colorClass = getSkillCategoryColor(index);
              
              return (
                <div 
                  key={skillCategory.id}
                  className="bg-white rounded-xl shadow-md hover:shadow-lg transition-all duration-300 p-6 transform hover:scale-[1.02]"
                >
                  <div className="flex items-center gap-3 mb-6">
                    <div className={`p-3 rounded-lg ${colorClass}`}>
                      <Icon className="w-6 h-6" />
                    </div>
                    <h3 className="text-lg font-bold text-gray-900">
                      {skillCategory.category}
                    </h3>
                  </div>

                  <div className="flex flex-wrap gap-2">
                    {skillCategory.skills && skillCategory.skills.length > 0 ? (
                      skillCategory.skills.map((skill, skillIndex) => (
                        <span
                          key={skillIndex}
                          className="px-3 py-1.5 bg-gray-50 text-gray-700 text-sm rounded-full font-medium hover:bg-blue-50 hover:text-blue-700 transition-colors cursor-default border border-gray-200 hover:border-blue-200"
                        >
                          {skill}
                        </span>
                      ))
                    ) : (
                      <span className="text-gray-500 text-sm">No skills available</span>
                    )}
                  </div>
                </div>
              );
            })
          ) : (
            <div className="col-span-full">
              <div className="bg-white rounded-xl shadow-md p-8">
                <p className="text-gray-600 text-center text-lg">No skills data available</p>
              </div>
            </div>
          )}
        </div>

        {/* Skills Highlight */}
        <div className="mt-16 bg-white rounded-xl shadow-md p-8">
          <div className="text-center mb-8">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">
              Core Competencies
            </h3>
            <p className="text-gray-600">
              Areas where I excel and continue to grow
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="text-center">
              <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <Code className="w-8 h-8 text-blue-600" />
              </div>
              <h4 className="font-semibold text-gray-900 mb-2">Full Stack Development</h4>
              <p className="text-sm text-gray-600">End-to-end web application development</p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <BarChart3 className="w-8 h-8 text-green-600" />
              </div>
              <h4 className="font-semibold text-gray-900 mb-2">AI/ML Integration</h4>
              <p className="text-sm text-gray-600">Intelligent systems and data analysis</p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <Database className="w-8 h-8 text-purple-600" />
              </div>
              <h4 className="font-semibold text-gray-900 mb-2">Database Design</h4>
              <p className="text-sm text-gray-600">Scalable data architecture</p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <Cloud className="w-8 h-8 text-orange-600" />
              </div>
              <h4 className="font-semibold text-gray-900 mb-2">Cloud Deployment</h4>
              <p className="text-sm text-gray-600">AWS and modern DevOps practices</p>
            </div>
          </div>
        </div>

        {/* Learning & Growth */}
        <div className="mt-12 text-center">
          <div className="bg-blue-50 rounded-xl p-8">
            <h3 className="text-xl font-bold text-gray-900 mb-4">
              Continuous Learning
            </h3>
            <p className="text-gray-700 max-w-2xl mx-auto">
              Technology evolves rapidly, and so do I. Currently exploring advanced AI/ML techniques, 
              cloud-native architectures, and emerging web technologies to stay at the forefront of innovation.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Skills;