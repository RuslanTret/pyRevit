﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace pyRevitManager.Properties {
    using System;
    
    
    /// <summary>
    ///   A strongly-typed resource class, for looking up localized strings, etc.
    /// </summary>
    // This class was auto-generated by the StronglyTypedResourceBuilder
    // class via a tool like ResGen or Visual Studio.
    // To add or remove a member, edit your .ResX file then rerun ResGen
    // with the /str option, or rebuild your VS project.
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("System.Resources.Tools.StronglyTypedResourceBuilder", "15.0.0.0")]
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    internal class Resources {
        
        private static global::System.Resources.ResourceManager resourceMan;
        
        private static global::System.Globalization.CultureInfo resourceCulture;
        
        [global::System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1811:AvoidUncalledPrivateCode")]
        internal Resources() {
        }
        
        /// <summary>
        ///   Returns the cached ResourceManager instance used by this class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Resources.ResourceManager ResourceManager {
            get {
                if (object.ReferenceEquals(resourceMan, null)) {
                    global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("pyRevitManager.Properties.Resources", typeof(Resources).Assembly);
                    resourceMan = temp;
                }
                return resourceMan;
            }
        }
        
        /// <summary>
        ///   Overrides the current thread's CurrentUICulture property for all
        ///   resource lookups using this strongly typed resource class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Globalization.CultureInfo Culture {
            get {
                return resourceCulture;
            }
            set {
                resourceCulture = value;
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Usage:
        ///    pyrevit help
        ///    pyrevit (-h | --help)
        ///    pyrevit (-V | --version)
        ///    pyrevit (blog | docs | source | youtube | support)
        ///    pyrevit env [--json] [--help] [--log=&lt;log_file&gt;]
        ///    pyrevit clone --help
        ///    pyrevit clone &lt;clone_name&gt; &lt;deployment_name&gt; [--dest=&lt;dest_path&gt;] [--source=&lt;archive_url&gt;] [--branch=&lt;branch_name&gt;] [--log=&lt;log_file&gt;]
        ///    pyrevit clone &lt;clone_name&gt; [--dest=&lt;dest_path&gt;] [--source=&lt;repo_url&gt;] [--branch=&lt;branch_name&gt;] [--log=&lt;log_file&gt;]
        ///	pyrevit clone &lt;clone_name&gt; --imag [rest of string was truncated]&quot;;.
        /// </summary>
        internal static string UsagePatterns {
            get {
                return ResourceManager.GetString("UsagePatterns", resourceCulture);
            }
        }
    }
}