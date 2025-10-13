import React from 'react';
import { personalInfo } from '../data/mock';
import { Github, Linkedin, Mail, Heart, ArrowUp } from 'lucide-react';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const socialLinks = [
    {
      icon: Github,
      href: personalInfo.github,
      label: 'GitHub'
    },
    {
      icon: Linkedin,
      href: personalInfo.linkedin,
      label: 'LinkedIn'
    },
    {
      icon: Mail,
      href: `mailto:${personalInfo.email}`,
      label: 'Email'
    }
  ];

  return (
    <footer className="bg-gray-900 text-white relative">
      <div className="max-w-6xl mx-auto px-6 py-12">
        <div className="grid md:grid-cols-3 gap-8 items-center">
          {/* Brand */}
          <div className="text-center md:text-left">
            <h3 className="text-2xl font-bold mb-2">Shreya Padaganur</h3>
            <p className="text-gray-400">
              Full Stack Developer & AI/ML Engineer
            </p>
          </div>

          {/* Social Links */}
          <div className="flex justify-center gap-6">
            {socialLinks.map((social, index) => {
              const Icon = social.icon;
              return (
                <a
                  key={index}
                  href={social.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="p-3 bg-gray-800 rounded-lg hover:bg-blue-600 transition-all duration-200 hover:scale-110 transform group"
                  aria-label={social.label}
                >
                  <Icon className="w-5 h-5 group-hover:text-white" />
                </a>
              );
            })}
          </div>

          {/* Contact Info */}
          <div className="text-center md:text-right">
            <p className="text-gray-400 mb-2">{personalInfo.location}</p>
            <a 
              href={`mailto:${personalInfo.email}`}
              className="text-blue-400 hover:text-blue-300 transition-colors"
            >
              {personalInfo.email}
            </a>
          </div>
        </div>

        {/* Divider */}
        <div className="border-t border-gray-800 my-8"></div>

        {/* Bottom Section */}
        <div className="flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="flex items-center gap-2 text-gray-400">
            <span>© {currentYear} Shreya Padaganur. Made with</span>
            <Heart className="w-4 h-4 text-red-500 fill-current" />
            <span>and lots of ☕</span>
          </div>

          <div className="flex items-center gap-6">
            <p className="text-sm text-gray-400">
              Built with React & FastAPI
            </p>
            
            {/* Back to Top */}
            <button
              onClick={scrollToTop}
              className="p-2 bg-gray-800 rounded-lg hover:bg-blue-600 transition-all duration-200 hover:scale-110 transform group"
              aria-label="Back to top"
            >
              <ArrowUp className="w-4 h-4 group-hover:text-white" />
            </button>
          </div>
        </div>
      </div>

      {/* Background Pattern */}
      <div className="absolute inset-0 opacity-5">
        <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-br from-blue-900 to-gray-900"></div>
      </div>
    </footer>
  );
};

export default Footer;