import React, { useState, useMemo } from 'react';
import { projectsApi } from '../services/api';
import { useApi } from '../hooks/useApi';
import { Github, ExternalLink, Code, Brain, Layers } from 'lucide-react';
import { Button } from './ui/button';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { LoadingSection, LoadingCard } from './LoadingSpinner';
import ErrorMessage from './ErrorMessage';

const Projects = () => {
  const [selectedCategory, setSelectedCategory] = useState('All');
  const { data: projects, loading, error, refetch } = useApi(() => projectsApi.getAll());
  
  // Get unique categories from projects
  const categories = useMemo(() => {
    if (!projects) return ['All'];
    const uniqueCategories = [...new Set(projects.map(project => project.category))];
    return ['All', ...uniqueCategories];
  }, [projects]);
  
  const filteredProjects = useMemo(() => {
    if (!projects) return [];
    return selectedCategory === 'All' 
      ? projects 
      : projects.filter(project => project.category === selectedCategory);
  }, [projects, selectedCategory]);

  const getCategoryIcon = (category) => {
    switch (category) {
      case 'AI/ML':
        return <Brain className="w-4 h-4" />;
      case 'Full Stack':
        return <Layers className="w-4 h-4" />;
      default:
        return <Code className="w-4 h-4" />;
    }
  };

  // Handle loading state
  if (loading) {
    return (
      <section id="projects" className="py-20 bg-white">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
              Featured Projects
            </h2>
            <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Showcasing innovative solutions in AI/ML and full-stack development
            </p>
          </div>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
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
      <section id="projects" className="py-20 bg-white">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
              Featured Projects
            </h2>
            <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
          </div>
          <ErrorMessage message={error} onRetry={refetch} />
        </div>
      </section>
    );
  }

  return (
    <section id="projects" className="py-20 bg-white">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
            Featured Projects
          </h2>
          <div className="w-24 h-1 bg-blue-600 mx-auto mb-8"></div>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Showcasing innovative solutions in AI/ML and full-stack development
          </p>
        </div>

        {/* Category Filter */}
        {categories.length > 1 && (
          <div className="flex justify-center mb-12">
            <div className="flex gap-2 bg-gray-100 p-1 rounded-lg">
              {categories.map((category) => (
                <button
                  key={category}
                  onClick={() => setSelectedCategory(category)}
                  className={`px-6 py-2 rounded-md font-medium transition-all duration-200 ${
                    selectedCategory === category
                      ? 'bg-blue-600 text-white shadow-md'
                      : 'text-gray-600 hover:text-gray-900 hover:bg-white'
                  }`}
                >
                  {category}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Projects Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredProjects && filteredProjects.length > 0 ? (
            filteredProjects.map((project) => (
              <Card 
                key={project.id}
                className="group hover:shadow-xl transition-all duration-300 transform hover:scale-[1.02] border-0 shadow-md"
              >
                <CardHeader className="p-0">
                  <div className="relative overflow-hidden rounded-t-lg">
                    <img
                      src={project.image}
                      alt={project.title}
                      className="w-full h-48 object-cover transition-transform duration-300 group-hover:scale-110"
                      onError={(e) => {
                        e.target.src = 'https://via.placeholder.com/600x400/f3f4f6/6b7280?text=' + encodeURIComponent(project.title);
                      }}
                    />
                    <div className="absolute top-4 right-4">
                      <Badge 
                        variant="secondary" 
                        className="bg-white/90 text-gray-900 backdrop-blur-sm flex items-center gap-1"
                      >
                        {getCategoryIcon(project.category)}
                        {project.category}
                      </Badge>
                    </div>
                  </div>
                </CardHeader>
                
                <CardContent className="p-6">
                  <CardTitle className="text-xl font-bold text-gray-900 mb-3 group-hover:text-blue-600 transition-colors">
                    {project.title}
                  </CardTitle>
                  <CardDescription className="text-gray-600 mb-4 line-clamp-3">
                    {project.description}
                  </CardDescription>
                  
                  {/* Technologies */}
                  <div className="flex flex-wrap gap-2 mb-4">
                    {project.technologies.slice(0, 4).map((tech, index) => (
                      <Badge key={index} variant="outline" className="text-xs">
                        {tech}
                      </Badge>
                    ))}
                    {project.technologies.length > 4 && (
                      <Badge variant="outline" className="text-xs">
                        +{project.technologies.length - 4} more
                      </Badge>
                    )}
                  </div>
                  
                  {/* Features Preview */}
                  <div className="space-y-2">
                    <h4 className="font-semibold text-sm text-gray-900">Key Features:</h4>
                    <ul className="text-sm text-gray-600 space-y-1">
                      {project.features.slice(0, 3).map((feature, index) => (
                        <li key={index} className="flex items-start gap-2">
                          <div className="w-1.5 h-1.5 bg-blue-600 rounded-full mt-2 flex-shrink-0"></div>
                          {feature}
                        </li>
                      ))}
                    </ul>
                  </div>
                </CardContent>
                
                <CardFooter className="p-6 pt-0 flex gap-3">
                  <Button 
                    variant="outline" 
                    size="sm" 
                    className="flex-1 hover:bg-blue-50 hover:border-blue-300 hover:text-blue-600"
                    onClick={() => window.open(project.github, '_blank')}
                  >
                    <Github className="w-4 h-4 mr-2" />
                    Code
                  </Button>
                  <Button 
                    size="sm" 
                    className="flex-1 bg-blue-600 hover:bg-blue-700"
                    onClick={() => window.open(project.demo, '_blank')}
                  >
                    <ExternalLink className="w-4 h-4 mr-2" />
                    Demo
                  </Button>
                </CardFooter>
              </Card>
            ))
          ) : (
            <div className="col-span-full">
              <div className="bg-gray-50 rounded-xl p-8 text-center">
                <p className="text-gray-600 text-lg">
                  {selectedCategory === 'All' 
                    ? 'No projects available at the moment.' 
                    : `No projects found in the "${selectedCategory}" category.`
                  }
                </p>
              </div>
            </div>
          )}
        </div>

        {/* Call to Action */}
        <div className="text-center mt-16">
          <div className="bg-gray-50 rounded-xl p-8">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">
              Interested in Learning More?
            </h3>
            <p className="text-gray-600 mb-6 max-w-2xl mx-auto">
              Each project represents a unique challenge and learning experience. 
              I'd be happy to discuss the technical details, architecture decisions, and lessons learned.
            </p>
            <Button 
              className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3"
              onClick={() => {
                const contactSection = document.querySelector('#contact');
                if (contactSection) {
                  contactSection.scrollIntoView({ behavior: 'smooth' });
                }
              }}
            >
              Let's Discuss My Work
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Projects;