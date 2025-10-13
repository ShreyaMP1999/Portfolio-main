import React from 'react';
import { experienceApi, educationApi } from '../services/api';
import { useApi } from '../hooks/useApi';
import { Building2, Calendar, MapPin, Briefcase, GraduationCap } from 'lucide-react';
import { LoadingSection, LoadingCard } from './LoadingSpinner';
import ErrorMessage from './ErrorMessage';

const Experience = () => {
  const { data: experience, loading: expLoading, error: expError, refetch: refetchExp } = useApi(() => experienceApi.getAll());
  const { data: education, loading: eduLoading, error: eduError, refetch: refetchEdu } = useApi(() => educationApi.getAll());

  // Handle loading state
  if (expLoading || eduLoading) {
    return (
      <section id="experience" className="py-20 bg-gray-50">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
              Professional Experience
            </h2>
            <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              My journey through impactful roles in technology and consulting
            </p>
          </div>
          <div className="space-y-12">
            <LoadingCard />
            <LoadingCard />
          </div>
        </div>
      </section>
    );
  }

  // Handle error state
  if (expError || eduError) {
    return (
      <section id="experience" className="py-20 bg-gray-50">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
              Professional Experience
            </h2>
            <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
          </div>
          <ErrorMessage 
            message={expError || eduError} 
            onRetry={() => {
              if (expError) refetchExp();
              if (eduError) refetchEdu();
            }} 
          />
        </div>
      </section>
    );
  }

  return (
    <section id="experience" className="py-20 bg-gray-50">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
            Professional Experience
          </h2>
          <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            My journey through impactful roles in technology and consulting
          </p>
        </div>

        <div className="space-y-12">
          {experience && experience.length > 0 ? (
            experience.map((job) => (
              <div 
                key={job.id}
                className="bg-white rounded-xl shadow-md hover:shadow-lg transition-all duration-300 p-8 transform hover:scale-[1.02]"
              >
                <div className="flex flex-col lg:flex-row lg:items-start gap-6">
                  {/* Company Info */}
                  <div className="lg:w-1/3">
                    <div className="flex items-center gap-3 mb-4">
                      <div className="p-3 bg-blue-50 rounded-lg">
                        <Building2 className="w-6 h-6 text-blue-600" />
                      </div>
                      <div>
                        <h3 className="text-xl font-bold text-gray-900">
                          {job.company}
                        </h3>
                        <div className="flex items-center gap-2 text-sm text-gray-600 mt-1">
                          <MapPin size={14} />
                          {job.location}
                        </div>
                      </div>
                    </div>
                    
                    <div className="space-y-2">
                      <div className="flex items-center gap-2 text-blue-600 font-semibold">
                        <Briefcase size={16} />
                        {job.position}
                      </div>
                      <div className="flex items-center gap-2 text-gray-600">
                        <Calendar size={16} />
                        {job.duration}
                      </div>
                      <div className="inline-block px-3 py-1 bg-gray-100 text-gray-700 text-sm rounded-full">
                        {job.type}
                      </div>
                    </div>
                  </div>

                  {/* Job Details */}
                  <div className="lg:w-2/3">
                    <h4 className="text-lg font-semibold text-gray-900 mb-4">
                      Key Responsibilities & Achievements
                    </h4>
                    <ul className="space-y-3 mb-6">
                      {job.responsibilities.map((responsibility, idx) => (
                        <li key={idx} className="flex items-start gap-3">
                          <div className="w-2 h-2 bg-blue-600 rounded-full mt-2 flex-shrink-0"></div>
                          <span className="text-gray-700 leading-relaxed">
                            {responsibility}
                          </span>
                        </li>
                      ))}
                    </ul>

                    {/* Technologies */}
                    <div>
                      <h5 className="font-semibold text-gray-900 mb-3">
                        Technologies Used
                      </h5>
                      <div className="flex flex-wrap gap-2">
                        {job.technologies.map((tech, idx) => (
                          <span 
                            key={idx}
                            className="px-3 py-1 bg-blue-50 text-blue-700 text-sm rounded-full font-medium hover:bg-blue-100 transition-colors cursor-default"
                          >
                            {tech}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ))
          ) : (
            <div className="bg-white rounded-xl shadow-md p-8">
              <p className="text-gray-600 text-center">No experience data available</p>
            </div>
          )}
        </div>

        {/* Education Section */}
        <div className="mt-20">
          <h3 className="text-3xl font-bold text-gray-900 text-center mb-12">
            Education
          </h3>
          
          <div className="grid md:grid-cols-2 gap-8">
            {education && education.length > 0 ? (
              education.map((edu) => (
                <div key={edu.id} className="bg-white rounded-xl shadow-md p-8 hover:shadow-lg transition-shadow duration-300">
                  <div className="flex items-center gap-3 mb-4">
                    <div className="p-3 bg-blue-50 rounded-lg">
                      <GraduationCap className="w-6 h-6 text-blue-600" />
                    </div>
                    <div>
                      <h4 className="text-lg font-bold text-gray-900">
                        {edu.degree}
                      </h4>
                      <p className="text-blue-600 font-medium">
                        {edu.school}
                      </p>
                    </div>
                  </div>
                  <div className="space-y-2 text-sm text-gray-600">
                    <div className="flex items-center gap-2">
                      <Calendar size={14} />
                      {edu.duration}
                    </div>
                    <div className="flex items-center gap-2">
                      <MapPin size={14} />
                      {edu.location}
                    </div>
                    <div className="font-semibold text-gray-700">
                      GPA: {edu.gpa}
                    </div>
                    {edu.achievements && edu.achievements.length > 0 && (
                      <div className="mt-3">
                        <h5 className="font-semibold text-gray-900 mb-2">Achievements:</h5>
                        <ul className="list-disc list-inside space-y-1">
                          {edu.achievements.map((achievement, idx) => (
                            <li key={idx} className="text-sm text-gray-600">{achievement}</li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </div>
                </div>
              ))
            ) : (
              <div className="col-span-2 bg-white rounded-xl shadow-md p-8">
                <p className="text-gray-600 text-center">No education data available</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Experience;